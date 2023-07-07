import re
import tkinter as tk

def arabic_to_roman(number):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_numeral = ''
    for numeral, letter in roman_numerals.items():
        while number >= numeral:
            roman_numeral += letter
            number -= numeral
    return roman_numeral

def convert():
    input_text = input_field.get()
    if input_text == "##":
        root.destroy()
    else:
        input_num = int(''.join(filter(str.isdigit, input_text)))
        if input_num >= 4000:
            output_field.config(text="Number must be less than 4000")
        else:
            input_text = input_text.replace(str(input_num), arabic_to_roman(input_num))
            output_field.config(text=input_text)

root = tk.Tk()
root.title("Arabic to Roman Converter")

# Input field
input_label = tk.Label(root, text="Enter a string:",font=('Times New Roman',15,'bold'),fg='green')
input_label.grid(row=0, column=0, padx=50, pady=90)
input_field = tk.Entry(root,font = ('Times New Roman',10,'bold'))
input_field.grid(row=0, column=1, padx=50, pady=59)

# Convert button
convert_button = tk.Button(root, text="Convert",font=('Cambria Math',15,'bold'),command=convert)
convert_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Output field
output_label = tk.Label(root, text="Converted string:",font=('Arial Black',10),fg='red')
output_label.grid(row=2, column=0, padx=50, pady=50)
output_field = tk.Label(root, text="",font=('Bookman Old Style',15,'bold'),fg = 'blue')
output_field.grid(row=2, column=1, padx=50, pady=50)

root.mainloop()