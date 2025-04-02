import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import wordcounter, letter_dictionary, dictionaries_list, sort_on


def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()
def main():
	book_path =  sys.argv[1]
	book = get_book_text(book_path)
	num_words = wordcounter(book)
	character_dictionary = letter_dictionary(book)
	char_list = dictionaries_list(character_dictionary)

	print("=========== BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ---------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	
	for item in char_list:
		print(f"{item['char']}: {item['count']}")
	
	print("============= END ==============")

if __name__ == "__main__":
	main()
