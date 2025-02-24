def count_words(file):
    word_list = file.split()
    word_count = len(word_list)
    return word_count

def character_counter(file):
    char_dict = {}
    for char in file.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else: 
            char_dict[char] += 1
    return char_dict

def sort_by_count(solo_dict):
    for key in solo_dict:
        return solo_dict[key]

def sorted_dict(char_dict):
    list_dict = [] 
    for letter in char_dict:
        if letter.isalpha():
            new_dict = {letter:char_dict[letter]}
            list_dict.append(new_dict) 
    list_dict.sort(reverse=True, key=sort_by_count)
    return list_dict
