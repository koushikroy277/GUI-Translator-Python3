from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()

# Size and Title
root.title("My personal translator")
root.geometry('550x350')
root.minsize(550, 350)

# Translating function
def translate():
	language_1 = t1.get("1.0", "end-1c")
	cl = choose_language.get()

	if language_1 == "":
		messagebox.showerror(
			"Language Translator","Please fill up the box")

	else:
		translator = Translator()
		output = translator.translate(language_1, dest=cl)
		t2.insert('end', output.text)

# Deleting the words
def clear():
	t2.delete(1.0, 'end')
	t2.delete(1.0, 'end')

img = ImageTk.PhotoImage(Image.open('google translate.png'))

label = Label(image=img)
label.place(x=230, y=3)

a = tk.StringVar()

auto_detect = ttk.Combobox(root, width = 20, textvariable = a, state = "readonly", font=('sans-serif', 10, 'bold'))
auto_detect['values'] = ('Auto Detect')
auto_detect.place(x=30, y=70)
auto_detect.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(root, width=20, textvariable = l, state='readonly', font=('Times New Roman', 10, 'bold'))

choose_language['values'] = ('English', 'Bengali', 'Hindi', 'Chinese', 'Japanese', 'French', 'Urdu', 'Turkese', 'Spanish', 'Arabian', 'Telugu', 'Tamil', 'Malayalam', 'Kannada', 'Indonesian', 'German', 'Polish', 'Swiss', 'Swedish')

choose_language.place(x=290, y=70)
choose_language.current(0)

t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

button = Button(root, text="Translate", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor='hand2', command=translate)
button.place(x=150, y=280)

clear = Button(root, text='Clear', relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor= 'hand2', command=clear)
clear.place(x=280, y=280)


root.mainloop()
