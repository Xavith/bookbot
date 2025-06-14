def number_of_words(text):
    list = text.split()
    return len(list)

def number_of_characters(text):
    chars = {}
    for a in text:
        low_case_text = a.lower()
        if low_case_text in chars:
            chars[low_case_text] += 1
        else:
            chars[low_case_text] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def dict_sorted(char_num_dict):
    sorted_list = []
    for b in char_num_dict:
        sorted_list.append({"char": b, "num": char_num_dict[b]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
