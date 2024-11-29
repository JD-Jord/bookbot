def main():
    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    num_words = get_numbers(text)
    characters = char_appearances(text)
    characters_list = dict_to_list(characters)
    characters_list.sort(reverse=True, key=dict_sort)
    print(f"--- Begin report of {book_path} --- \n{num_words} words found in the document")
    for d in characters_list:
        for k,v in d.items():
            print(f"The '{k}' character was found {v} times")
def read_text(path):
    with open(path) as f:
        return f.read()

def get_numbers(text):
    words = text.split()
    return len(words)

def char_appearances(text):
    text = text.lower()
    dict = {}
    for c in set(text):
        dict[c] = text.count(c)
    return dict

def dict_sort(dict):
    return list(dict.values())[0]

def dict_to_list(dict):
    dict_list = []
    for key, value in dict.items():
        if key.isalpha() == True:
            new_dict = {key: value}
            dict_list.append(new_dict)
    return dict_list


main()