def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Frankenstein book has {num_words} words")
    counted_letters = count_letters(text)
    print(f"Each occurence of a letter in Frankenstein:\n {counted_letters}")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    letters = {}
    nocap = text.lower()
    for i in nocap:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters



main()