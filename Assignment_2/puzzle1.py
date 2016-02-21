sys_words = set()

with open('/usr/share/dict/words', 'r') as f:
	for line in f:
		sys_words.add(line[:-1])

sys_words_itr = iter(sys_words)

# for i in range(10):
# 	print(next(sys_words_itr))

diff_words = []

with open('words.txt', 'r') as f:
	for line in f:
		word = line[:-1]
		if word not in sys_words and len(word) > 3:
			diff_words.append(word)

for word in diff_words:
	if len(word) == 17:
		print(word + " ")

print("len: {0}".format(len(diff_words)))