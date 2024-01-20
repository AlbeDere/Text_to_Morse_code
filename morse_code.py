def read_morse_code_dict(file_path):
    morse_code_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            morse_code_dict[key] = value
    return morse_code_dict

if __name__ == "__main__":
    morse_code_dict_file = "morse_code_dict.txt"
    morse_code_dict = read_morse_code_dict(morse_code_dict_file)

    input_text = input("Enter the text to convert to Morse code: ")
    
    morse_code_list = []
    for char in input_text.upper():
        if char in morse_code_dict:
            morse_code_list.append(morse_code_dict[char])
        else:
            morse_code_list.append(char)

    morse_code_result = ' '.join(morse_code_list)
    print(f"Morse Code: {morse_code_result}")