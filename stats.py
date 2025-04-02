def wordcounter(book):
        words = len(book.split())
        return words

def letter_dictionary(book):
	character_counts = {}
	lower_text = book.lower()
	for char in lower_text:
		if char.isalpha():
			character_counts[char] = character_counts.get(char, 0) + 1
	return character_counts

def dictionaries_list(dict):
	list = []
	for k in dict:
		dictionary = {"char": k, "count": dict[k]}
		list.append(dictionary)
	list.sort(reverse=True, key=sort_on)	
	return list

def sort_on(dict):
	return(dict["count"])
