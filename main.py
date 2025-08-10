import sys
from stats import get_word_count
from stats import get_character_counts
from stats import get_sorted_dictionary_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    contents = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    num_words = get_word_count(contents)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    character_counts = get_character_counts(contents)
    sorted_chars = get_sorted_dictionary_list(character_counts)

    for c in sorted_chars:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")

    print("============= END ===============")

def get_book_text(file_path):
    contents = ""
    with open(file_path) as f:
        contents = f.read()
    return contents

main()