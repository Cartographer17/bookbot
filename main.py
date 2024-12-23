def wordchar_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
    word_list = file_contents.split()
    lowered_string=file_contents.lower()
    input_dict={}
    for char in lowered_string:
        if char.isalpha():
            input_dict[char] = input_dict.get(char, 0) + 1
    sorted_dict= sorted(input_dict.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {path_to_file} ---\n{len(word_list)} words found in the document\n") 
    for entry in sorted_dict:   
        print(f"The '{entry[0]}' character was found {entry[1]} times")
    print("--- End report ---") 
    
    



def main():
    path_to_file = 'books/frankenstein.txt'
    wordchar_count(path_to_file)


if __name__ == "__main__":
    main()