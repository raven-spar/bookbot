def find__num_words(text):
    words = text.split()
    count = len(words)
    return count

def find_num_char(text):
    text = text.lower()
    char_dict = {}
    for i in text:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]
def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for key in char_dict:
        sorted_list.append({"char": key , "num": char_dict[key]})
    sorted_list.sort(reverse=True , key = sort_on)
    return sorted_list

def main():
    location = "books/frankistein.txt"
    content = get_file_contents(location)
    num_words = find__num_words(content)
    num_char = find_num_char(content)
    sorted_list = char_dict_to_sorted_list(num_char)

    print(f"--- Begin Report of {location}---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']} charecter was found {item['num']} times")

main()