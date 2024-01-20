import tkinter as tk

def read_morse_code_dict(file_path):
    morse_code_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            morse_code_dict[key] = value
    return morse_code_dict

def convert_to_morse_code():
    input_text = entry.get()
    
    morse_code_list = []
    error_message = ""
    for char in input_text.upper():
        if char in morse_code_dict:
            morse_code_list.append(morse_code_dict[char])
        # If the character is not found add it to error message
        else:
            error_message += f"Error: No Morse code for character '{char}'.\n"

    morse_code_result = ' '.join(morse_code_list)

    if error_message:
        result_label.config(text=error_message)
    else:
        result_label.config(text=f"Morse Code: {morse_code_result}")

morse_code_dict_file = "morse_code_dict.txt"
morse_code_dict = read_morse_code_dict(morse_code_dict_file)

# UI
window = tk.Tk()
window.title("Morse Code Converter")

label = tk.Label(window, text="Enter text to convert:")
label.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_to_morse_code)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()