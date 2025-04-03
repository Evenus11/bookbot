def word_count (string_of_file):
    list_of_split=string_of_file.split()
    length = len(list_of_split)
    return length

def character_count (text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count: 
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list=[]
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


