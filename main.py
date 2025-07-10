import sys
from stats import sorting
from stats import char_counter
from stats import get_num_words
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
with open(sys.argv[1]) as f:
	file_contents = f.read()
counter = get_num_words(file_contents)
themessage = "Found " + str(counter) + " total words"
bookdict = char_counter(file_contents)
sorted = sorting(bookdict)
#sorted = sorter.isalpha()
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count ----------")
print(themessage)
print("--------- Character Count -------")
#print(bookdict)
for entry in sorted:
	print(f"{entry['char']}: {entry['num']}")
print("============= END ===============")

#print(themessage)
#from stats import get_num_words

