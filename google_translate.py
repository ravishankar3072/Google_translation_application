from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to convert language name to its corresponding code
def get_language_code(lang_name):
    for code, name in LANGUAGES.items():
        if name.lower() == lang_name.lower():
            return code
    return None  # If language not found (should not happen with correct inputs)

# Function to translate text
def translate_text():
    src_lang = get_language_code(comb_sor.get())  # Convert language name to code
    dest_lang = get_language_code(comb_dest.get())

    if not src_lang or not dest_lang:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, "Error: Invalid Language Selection")
        return

    text_to_translate = Sor_txt.get(1.0, END).strip()  # Get text from input
    if not text_to_translate:
        return

    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=src_lang, dest=dest_lang).text

    dest_txt.delete(1.0, END)
    dest_txt.insert(END, translated_text)

# Main UI Window
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

# Heading
Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg="Red").place(x=100, y=40, height=50, width=300)

# Source Text Label
Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Red").place(x=100, y=100, height=20, width=300)

# Source Text Box
Sor_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

# Language Selection
language_list = list(LANGUAGES.values())  # Get language names

# Source Language Combobox
comb_sor = ttk.Combobox(root, value=language_list, state="readonly")
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("English")  # Default selection

# Translate Button
Button(root, text="Translate", relief=RAISED, command=translate_text).place(x=170, y=300, height=40, width=150)

# Destination Language Combobox
comb_dest = ttk.Combobox(root, value=language_list, state="readonly")
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("Hindi")  # Default selection

# Destination Text Label
Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Red").place(x=100, y=360, height=20, width=300)

# Destination Text Box
dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

# Module Installation Info
Label(root, text="Module Required", font=("Times New Roman", 20, "bold"), bg="Red").place(x=100, y=570, height=50, width=300)
Label(root, text="pip install googletrans==3.1.0a0", bg="Red", font=("Times New Roman", 16, "bold")).place(x=0, y=620, height=50, width=500)

root.mainloop()
