strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for word in strings:
	sentence += str(word) + " "
print(sentence[:-1])