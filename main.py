def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_chars = generate_report(text)
    print(num_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def generate_report(text):
    # Convert the text to upper case so we can ignore case
    upper_text = text.upper()

    # Create a dictionary to store the counts of each character
    map = {}

    for char in upper_text:
        if char.isalpha():
            map[char] = map.get(char, 0) + 1

    # Convert the map into a list of tuples
    char_list = list(map.items())

    # Sort the list by the count of each character
    char_list.sort(key=lambda x: x[1], reverse=True)

    report = f"--- Begin book report ---\n"
    num_words = count_words(text)
    report += f"There are {num_words} words in the book.\n\n"

    for char, count in char_list:
        report += f"The '{char}' character was found {count} times\n"
    
    report += "\n--- End book report ---"
    
    return report

main()