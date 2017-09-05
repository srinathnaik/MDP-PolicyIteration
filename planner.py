import sys
from numpy import linalg as LA
import numpy as np
import copy
from pulp import *
import random

arguments = sys.argv[1:]
get={'--mdp':None, '--algorithm':None, '--batchsize':None, '--randomseed':None}

states=None
actions=None
transisition=[]
reward=[]
gamma=None
# fill the arguments
i=0;
while i<len(arguments):
	if arguments[i] in get:
		get[arguments[i]]=arguments[i+1]
		i = i+2
	else:
		i=i+1

# fill the variables from the file
f = open(get['--mdp'],'r')
states=int(f.readline())
actions=int(f.readline())
for s in range(0,states):
	ac = []
	for a in range(0,actions):
		lin=[]
		lin = (f.readline()).split("\t")
		del lin[-1]
		lin = [float(x) for x in lin]
		ac.append(lin)
	reward.append(ac)

for s in range(0,states):
	ac = []
	for a in range(0,actions):
		lin=[]
		lin = (f.readline()).split("\t")
		del lin[-1]
		lin = [float(x) for x in lin]
		ac.append(lin)
	transisition.append(ac)

gamma = float(f.readline());

# print "given values"
# print states
# print actions
# print transisition
# print reward
# print gamma

# some variables and their initialisation
V = [0.0 for i in range(states)] 					# the value function
Q = [[0.0,0.0] for i in range(states) ] 			# action-value function Q(s,a) to access
policy = [0 for i in range(states)] 				# the initial policy
improve = [1 for i in range(states)] 				# improve[i] says weather state i is improvisable or not
improve_action = [None for i in range(states)] 		# the improvising action
improve_batches=[]									# the batches that can be improved
batch_size = None									# the batch size provided
total_policies=0									# total policies searched for, to find the optimal

""" The helper functions """

def maxNorm(A,B):							# calculates maximum difference norm
	maxi = -float('inf')
	for s in range(states):
		maxi = max(maxi,abs(A[s]-B[s]))
	return maxi

def ploicyEvaluate():						# evaluates the policy and values are stored in V
	v=[0 for i in range(states)]       		# initialization
	delta = 0.0000000001                    # convergence precision
	converged = False
	while not converged:
		v_old = copy.copy(v)
		for s in range(states):
			summ=0.0
			for s_n in range(states):
				summ += transisition[s][policy[s]][s_n] * (reward[s][policy[s]][s_n]+gamma*v_old[s_n])
			v[s] = summ
		# print maxNorm(v,v_old)
		if(maxNorm(v,v_old)<delta):
			converged = True
	global V
	V = copy.copy(v)
	global total_policies
	total_policies += 1

def actionValueEvaluate():					# calculates the action-value function Q
	global Q
	for s in range(states):
		for a in range(actions):
			summ=0.0
			for s_n in range(states):
				summ += transisition[s][a][s_n] * (reward[s][a][s_n]+gamma*V[s_n])
			Q[s][a] = summ

def myBatch(state):						    # given a state, returns its batch number (1-indexed)
	ss = (state+1)/batch_size;
	if((state+1) % batch_size > 0):
		ss += 1
	return ss

def calculateImprovement():					# notes weather the states and corresponding batches are improvisable or not
	global improve
	global improve_action
	global improve_batches
	for s in range(states):
		improve[s]=0
		for a in range(actions):
			if Q[s][a]>Q[s][policy[s]]:
				improve[s]=1
				improve_action[s]=a
				if get['--algorithm'] == 'bspi':
					improve_batches[myBatch(s)]=1


def improvement():							# checks weather there is improvement in atleast one state
	for s in range(states):
		if improve[s]==1:
			return True
	return False

def improve_all():							# improve all states that are marked in calculateImprovement
	global policy
	for s in range(states):
		if improve[s]==1:
			policy[s]=improve_action[s]

def improve_some():							# improve uniformly selected random subset of states marked in calculateImprovement
	global policy
	picked = False
	while not picked:
		for s in range(states):
			if improve[s]==1 and random.random()>=0.5:
				picked = True
				policy[s]=improve_action[s]

def improve_last_improvable_batch():		# improve the last batch marked by calculateImprovement
	global policy
	sz = len(improve_batches)
	for b in xrange(sz-1,0,-1):
		if improve_batches[b]==1:
			low = batch_size*(b-1);
			high = min(states,(batch_size*b))
			# print low,high
			for s in range(low, high):
				if improve[s]==1:
					policy[s]=improve_action[s]
			break


def printpolicy(lp=None):							# printing the value and policy in desired format
	for s in range(states):
		# print '{0:.7f}'.format(V[s]),policy[s]
		print V[s],policy[s]
	# print "Iterations ", total_policies

""" The Algorithms """

def hpi(): 									# howards policy iteration
	finished = False
	while not finished:
		ploicyEvaluate()
		actionValueEvaluate()
		calculateImprovement()
		if improvement():
			improve_all()
		else:
			finished = True
	printpolicy()

def lp():									# linear programming approach
	prob = pulp.LpProblem("OptimalValue", pulp.LpMinimize)

	variables=[]
	for i in range(states):
		var = str('v'+str(i))
		var = pulp.LpVariable(str(var))
		variables.append(var)

	objective=""
	for s in range(states):
		objective+=variables[s]

	prob += objective

	for s in range(states):
		for a in range(actions):
			lhs = ""
			for s_n in range(states):
				lhs+=transisition[s][a][s_n]*reward[s][a][s_n]+ transisition[s][a][s_n]*gamma*variables[s_n]
			prob+=(lhs<=variables[s])
		
	# prob.writeLP("optimization.lp" )
	result = prob.solve()
	assert result == pulp.LpStatusOptimal

	global V
	for v in prob.variables():
		nme = v.name
		s = int(nme[1:])
		# print s,v.varValue
		V[s]=v.varValue

	actionValueEvaluate()
	calculateImprovement()
	if improvement():
		improve_all()
	printpolicy()

def rpi():									# randomized policy iteration
	finished = False
	while not finished:
		ploicyEvaluate()
		actionValueEvaluate()
		calculateImprovement()
		if improvement():
			improve_some()
		else:
			finished = True
	printpolicy()

def bspi():									# batch-switching policy iteration
	global improve_batches
	finished = False
	while not finished:
		ploicyEvaluate()
		actionValueEvaluate()
		improve_batches = [0 for i in improve_batches]
		calculateImprovement()
		if improvement():
			improve_last_improvable_batch()
		else:
			finished = True
	printpolicy()
	
# search for what algorithm is given
algo = get['--algorithm']
if algo is None:
	print "No algorithm given"
	sys.exit(-1)
elif algo=='lp':
	lp()
elif algo=='rpi':
	# print get['--randomseed']
	random.seed(int(get['--randomseed']))
	rpi()
elif algo=='bspi':
	# print get['--batchsize']
	batch_size = int(get['--batchsize'])
	batches = states/batch_size
	if(states%batch_size > 0):
		batches += 1
	improve_batches=[0 for i in range(batches+1)]
	bspi()

elif algo=='hpi':
	hpi()
else:
	print "We do not know the given algorithm"
	sys.exit(-1)