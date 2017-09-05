import random
import sys

random.seed(int(sys.argv[1]))
S=50
A=2
print S
print A

for s in range(0, S):
    for a in range(0, A):
    	ran_values = [random.uniform(-1,1) for i in range(0, S)]
        for sPrime in range(0, S):
            print str(ran_values[sPrime]) + "\t",

        print "\n",

for s in range(0, S):
    for a in range(0, A):
    	ran_values = [random.uniform(0,1) for i in range(0, S)]
    	summ = sum(ran_values)
        for sPrime in range(0, S):
            print str(ran_values[sPrime]/summ) + "\t",

        print "\n",

print random.uniform(0.89,1)