import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
from stats import get_book_text, count_words, count_char, count_sorter
def main():
    word_count = count_words(get_book_text(book_path))  


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    charcount = count_char(get_book_text(book_path))
    sorter = count_sorter(charcount)
    for words in sorter:
        character = words["char"]
        count = words["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")    
main()