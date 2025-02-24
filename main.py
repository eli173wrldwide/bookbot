import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_function(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    from stats import count_words, character_counter, sorted_dict, sort_by_count
    file_contents = get_book_function(sys.argv[1])
    word_count = count_words(file_contents)
    char_dict = character_counter(file_contents)
    sorted_chars = sorted_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...") # needs fixin
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            print(f"{char}: {count}")
    
    print("============= END ===============")

    return

main()


