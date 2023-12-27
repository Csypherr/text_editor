#==========================================================================================
#   Mela Bamiji.
#   26th December, 2023.
#
#   A simple text editor program that has just the basic functionalities of a text editor.
#   This program is meant for instructional uses only!
#===========================================================================================

import os 
from tkinter import RIGHT, Y, Button, Frame, Menu, OptionMenu, Scrollbar, Spinbox, StringVar, Text, Tk
from tkinter import filedialog, colorchooser, font
from tkinter.constants import N, E, S, W, END
from tkinter.messagebox import Message, showinfo
from tkinter.filedialog import FileDialog, SaveFileDialog, askopenfilename


def change_color():
    """Change the color of the font."""
    
    color = colorchooser.askcolor(title="pick a color...or else")
    text_area.config(fg=color[1])

def change_font(*args):
    """Change the font type."""
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    """Create a new file for editing."""
    
    window.title("*untitled")
    text_area.delete(1.0, END) 


def open_file():
    """File dialog: open an existing file."""
    
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")
        
        text_area.insert(1.0, file.read())
    except FileNotFoundError:
        print("Error reading file") 
    finally:
        file.close()


def save_file():
    """File dialog: save file to local disk."""
    
    file = filedialog.asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt', 
                                        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    
    if file is None:
        return 
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))

        except Exception:
            print("Error saving file")
        finally:
            file.close() 



def cut():
    """Remove a selected text."""
    
    text_area.event_generate("<<Cut>>")


def copy():
    """Copy a selected text to the clipboard."""
    
    text_area.event_generate("<<Copy>>")


def paste():
    """Place the selected text at the new location"""
    
    text_area.event_generate("<<Paste>>")


def about():
    """Access and display information about the application."""
    
    showinfo("About this program", "Simple Text Editor.\n Version 0.1.0")

def quit():
    """Exit the program."""
    
    window.destroy()


# instantiate the window, title
window = Tk()
window.title("Text Editior Application")

# define window width and height
window_width = 900
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# set x and y axis
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# set window geometry
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y)) 

# set the font proprties
font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("25")

# define the text area
text_area = Text(window, font=(font_name.get(), font_size.get()))

# define the scroll bar and configure the window text area 
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y) 
text_area.config(yscrollcommand=scroll_bar.set)

# define the window frame
frame = Frame(window)
frame.grid()

# create button to change color
color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

# create menu to list available fonts
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

# create widget to increase or decrease the font size
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# instantiate drop-down menus
menu_bar = Menu(window)
window.config(menu=menu_bar)

# create a file menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# create the edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# create the help menu
help_menu = Menu(menu_bar, tearoff=0) 
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About...", command=about)

# program's main loop
window.mainloop()