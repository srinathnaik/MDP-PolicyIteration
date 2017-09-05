import sys
file1 = sys.argv[1]
file2 = sys.argv[2]

f1=open(file1,'r')
f2=open(file2,'r')
j=0
k = False
for line2 in f2:
	line1 = f1.readline()
	line1 = line1.strip("\n")
	line2 = line2.strip("\n")
	line1 = line1.split()
	line2 = line2.split()
	assert len(line1)==len(line2)
	# if not (int(float(line1[0])*1000000) == int(float(line2[0])*1000000)):
	if not (format(float(line1[0]),'.7f') == format(float(line2[0]),'.7f')):
		k = True
		print "		",j,"original ",line1[0],line2[0]
	if not (line1[1] == line2[1]):
		print "		",j,"differ policy",line1[1],line2[1]
	j = j+1

if(not k):
	print "		OK"

print "		"+f1.readline().strip("\n")