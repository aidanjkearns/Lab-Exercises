import re

hand = open('mbox-short.txt')
x = list()
y = list()
for line in hand:
	#line = line.rstrip()
	x = x + re.findall('From(.*)', line)
	y = y + re.findall('[0-9]+', x)

print(x)
print(y)


#y = list()
#for entry in x:
	#y.append(float(entry))

#print('Number of Values:',len(y))
#print('Maximum:', max(y))
#print('Minimum:', min(y))
#avg = sum(y)/len(y)
#rounded = round(avg,3)
#print('Average:', rounded)

