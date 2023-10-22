from playsound import playsound
from tkinter import *
from tkinter import messagebox
import time

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '. _ _ _ .',
    '!': '_ . _ . _ _',
    '/': '_ . . _ .',
    '(': '_ . _ _ .',
    ')': '_ . _ _ . _',
    '&': '. _ . . .',
    ':': '_ _ _ . . .',
    ';': '_ . _ . _ .',
    '=': '_ . . . _',
    '+': '. _ . _ .',
    '-': '_ . . . . _',
    '_': '. . _ _ . _',
    '"': '. _ . . _ .',
    '$': '. . . _ . . _',
    '@': '. _ _ . _ .',
}


def text_to_morse():
    text = text_input.get()
    message_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            message_code += MORSE_CODE_DICT[char] + " "
        else:
            message_code += ' '
    morse_output.delete(0, END)
    return morse_output.insert(0, message_code.strip())


def play_morse_sound():
    if selected_option == 1:
        message_code = morse_output.get()
    else:
        message_code = morse_input.get()
    for char in message_code:
        if char == ".":
            playsound("short_beep.mp3")
            time.sleep(0.3)
        elif char == "-":
            playsound("long_beep.mp3")
            time.sleep(0.3)
        elif char == "/" or char == " ":
            time.sleep(0.5)
        else:
            messagebox.showinfo(title="Error", message=f"Invalid character in {message_code}")


def morse_to_text():
    morse_code = morse_input.get()
    morse_to_char = {morse: char for char, morse in MORSE_CODE_DICT.items()}
    words = morse_code.split('   ')
    translated_text = ''
    for word in words:
        chars = word.split()
        for i, char in enumerate(chars):
            if i == 0:
                translated_text += morse_to_char.get(char, '').upper()
            else:
                translated_text += morse_to_char.get(char, '').lower()
        translated_text += ' '

    text_output.delete(0, END)
    return text_output.insert(0, translated_text.strip())


def show_options():
    global text_input, morse_output, morse_input, text_output, selected_option
    selected_option = radio_state.get()

    if selected_option == 1:
        text_label = Label(text="Text to Morse: ")
        text_label.grid(column=0, row=1)
        text_label.focus()
        morse_label = Label(text="Morse Code: ")
        morse_label.grid(column=0, row=3)
        text_input = Entry(width=36)
        text_input.grid(column=2, row=1, columnspan=2)
        morse_output = Entry(width=36)
        morse_output.grid(column=2, row=3, columnspan=2)
        gen_button = Button(text="Generate", width=12, height=2, command=text_to_morse)
        gen_button.grid(column=2, row=4)
        playsound_button = Button(text="PlaySound", width=12, height=2, command=play_morse_sound)
        playsound_button.grid(column=3, row=4)
    else:
        morse_label = Label(text="Morse to text:")
        morse_label.grid(column=0, row=1)
        text_label = Label(text="Decoded text:")
        text_label.grid(column=0, row=3)
        text_label.focus()
        morse_input = Entry(width=36)
        morse_input.grid(column=2, row=1, columnspan=2)
        text_output = Entry(width=36)
        text_output.grid(column=2, row=3, columnspan=2)
        gen_button = Button(text="Generate", width=12, height=2, command=morse_to_text)
        gen_button.grid(column=2, row=4)
        playsound_button = Button(text="PlaySound", width=12, height=2, command=play_morse_sound)
        playsound_button.grid(column=3, row=4)


window = Tk()
window.title("Morse Code Convertor")
window.config(padx=50, pady=50)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Text to Morse", value=1, variable=radio_state, command=show_options)
radiobutton2 = Radiobutton(text="Morse to Text", value=2, variable=radio_state, command=show_options)

radiobutton1.grid(column=0, row=0)
radiobutton2.grid(column=1, row=0)

window.mainloop()
