def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    counts = {}    
    for i in range(0, len(text)):
        c = text[i].lower()
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def get_sorted_dictionary_list(dictionary):
    char_list = []
    for key in dictionary:
        c = {"char": key, "num": dictionary[key]}
        char_list.append(c)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(items):
    return items["num"];