def main():
    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    num_words = get_numbers(text)
    characters = char_appearances(text)
    print(f"{num_words} words found in the document")
    print(characters)

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


main()