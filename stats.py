def get_num_words(file_contents):
		numbers = 0
		stringing = file_contents.split()
		for i in stringing:
                	numbers +=1
		return numbers

def char_counter(file_contents):
	new_dict = {}
	counter = file_contents.lower()
	for letter in counter:
		if letter in new_dict:
			new_dict[letter] += 1
		else:
			new_dict[letter] = 1
	return new_dict

def sorting(new_dict):
	newer_dict = {}
	dictlist = []
	dictlist2 = []
	for char in new_dict:
		count = new_dict[char]
		entry = {"char": char, "num": count}
		if char.isalpha() == True:
			dictlist.append(entry)
	dictlist.sort(reverse=True, key=lambda x: x["num"])
	return dictlist

