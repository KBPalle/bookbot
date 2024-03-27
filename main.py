def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Frankenstein book has {num_words} words\n\n")
    
    
    counted_letters = count_letters(text)
    #print(f"Each occurence of a letter in Frankenstein:\n {counted_letters}")
    lst_letters = create_lst(counted_letters)
    lst_letters.sort(key=sort_on, reverse=True)
    report(lst_letters)


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
        if i.isalpha() == True:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    return letters


def create_lst(dict):
    counted_lst_letters = []
    for letter, count in dict.items():
        letter_dict = {"letter": letter, "count": count}
        counted_lst_letters.append(letter_dict)
    return counted_lst_letters

def sort_on(item):
    return item['count']

def report(sorted_list):
    print(f"________Begin Report________\n")
    for entry in sorted_list:
        letter = entry["letter"]
        count = entry["count"]
        print(f"The letter: {letter} was found {count} times")
    print("________End of report________")

main()