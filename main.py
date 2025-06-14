import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import (
    number_of_words,
    number_of_characters,
    dict_sorted,
)

def main():
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = number_of_words(file_contents)
    chars_dict = number_of_characters(file_contents)
    chars_sorted = dict_sorted(chars_dict)
    print_report(book_path, num_words, chars_sorted)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def print_report(path, num_words, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()