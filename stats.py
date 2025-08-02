def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        contents = f.read()
    return contents

def count_words(contents):
    word_count = len(contents.split())
    return word_count

def count_char(booktext):
    char_dict = {}
    booktext = booktext.lower()
    for char in booktext:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(words):
    return words["num"]

def count_sorter(dict):
    dictholder = []
    for char, count in dict.items():
        tempdict = {}
        tempdict["char"] = char
        tempdict["num"] = count
        dictholder.append(tempdict)
    dictholder.sort(reverse=True,key=sort_on)
    return dictholder
    
        

    