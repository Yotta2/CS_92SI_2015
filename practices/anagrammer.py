#words = ["python", "java", "google", "emc", "function"]

with open("/usr/share/dict/words", "r") as file:
	words = [word[:-1] for word in file]

dict = {} # sorted_form => list of words have the same sorted form

for word in words:
	sorted_form = "".join(sorted(word))
	if sorted_form not in dict:
		dict[sorted_form] = []
	dict[sorted_form] = word

def find_anagrams(letters):
	sorted_form = sorted(letters)
	return [word for word in words if sorted(word) == sorted_form]

while True:
	letters = input("Letters? ")
	print("Anagram(s): " + str(dict["".join(sorted(letters))]))

