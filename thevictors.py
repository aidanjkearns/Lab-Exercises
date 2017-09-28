victors = open('TheVictors.txt')
words = list()
for line in victors:
	for word in line.split():
		word.rsplit()
		words.append(word)
count = dict()
for word in words:
	if word not in count:
		count[word] = 1
	else:
		count[word] = count[word] + 1
l = list()
for key, val in count.items():
	l.append((val, key))
l.sort(reverse=True)
for key, val in l[:15]:
	print(val, key)

 







