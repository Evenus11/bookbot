from stats import word_count
from stats import character_count
from stats import chars_dict_to_sorted_list
import sys

def get_book_text(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1] 
    text = get_book_text(path)
    num_words = word_count(text)
    charactors = character_count(text)
    list=chars_dict_to_sorted_list(charactors)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for item in list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()