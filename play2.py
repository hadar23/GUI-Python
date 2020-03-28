from tkinter import *
from exercise2 import *
from tkinter import scrolledtext


# function for showing the words by character and a boolean (include/exclude)
def show_words(character, include):
    if len(character) > 1:
        print("enter a character, not a word")
        return
    if not character.isalpha():
        print("enter a letter, not a sign or a digit")
        return
    generator_for_words = words_generator(character, include)
    word_textbox.delete(1.0, END)
    for inner_word in generator_for_words:
        word_textbox.insert(END, inner_word)
        word_textbox.insert(END, "\n")


# create the root frame
root = Tk()

# create the text box
word_textbox = scrolledtext.ScrolledText(root)
word_textbox.config(state=NORMAL)
word_textbox.pack(anchor=W)

# create the bottom frame
bottom_frame = Frame(root)
bottom_frame.pack(anchor=W, fill=BOTH)

# create the character label
character_label = Label(bottom_frame, text="Character: ")
character_label.pack(side=LEFT, padx=5)

# create the entry label
character_entry = Entry(bottom_frame)
character_entry.pack(side=LEFT, anchor=CENTER, padx=5)

# create the radio frame
radio_frame = Frame(bottom_frame)
radio_frame.pack(side=LEFT, padx=5)

# the boolean variable
include_choice = BooleanVar()

# include radio button
include_radio = Radiobutton(radio_frame, text="Include", variable=include_choice, value=True)
include_radio.pack(anchor=W)

# exclude radio button
exclude_radio = Radiobutton(radio_frame, text="Exclude", variable=include_choice, value=False)
exclude_radio.pack(anchor=W)

# the "show words" button
show_button = Button(bottom_frame, text="Show Words",
                     command=lambda: show_words(character_entry.get(), include_choice.get()))
show_button.pack(side=LEFT, anchor=CENTER, padx=5)

# the "show graph" button
show_button = Button(bottom_frame, text="Show Graph",
                     command=lambda: show_graph())
show_button.pack(side=LEFT, anchor=CENTER, padx=5)


# start the GUI
root.mainloop()
