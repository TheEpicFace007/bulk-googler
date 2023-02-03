import os
import time
import webbrowser
import urllib.parse
import tkinter
import tkinter.messagebox
import sys
from tkinter import ttk
import traceback

from rich import print
from PIL import Image, ImageTk

if not os.path.exists("./bulkgoogling.txt"):
    with open('./bulkgoogling.txt', 'w') as f:
        f.write('')
        print("./bulkgoogling.txt created, please add the keywords you want to search for in bulk")
        exit(0)


def google(keywords):
    webbrowser.open('https://www.google.com/search?q=' +
                    urllib.parse.quote(keywords), 0, False)
    time.sleep(0.05)


def bulkgoogle():
    with open('./bulkgoogling.txt', 'r') as f:
        keywords = f.read().splitlines()
        for kw in keywords:
            print("[bold]Searching for[/bold] [underline]" + kw + "[/underline]")
            google(kw)


class MainFrame(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Bulk Googler")
        # Set the icon
        self.wm_iconphoto(True, tkinter.PhotoImage(file='icon.png'))
        # When the user press supprr or backspace, remove the keyword
        self.bind("<Delete>", lambda event: self.remove_keyword())
        self.bind("<BackSpace>", lambda event: self.remove_keyword())

        self.create_variables()
        self.create_widgets()
        self.create_layout()

    def create_variables(self):
        self.keywords = tkinter.StringVar()  # Text to search for

    def create_widgets(self):
        self.keywordsLabel = tkinter.Label(self, text="Keywords: ")
        self.keywordsLabel.grid(row=0, column=0, sticky="w")

        self.keywordsEntry = ttk.Entry(self, textvariable=self.keywords)
        self.keywordsEntry.grid(row=0, column=1, sticky="ew", padx=5)
        self.keywordsEntry.config(width=40)
        # When the user presses enter, add the keyword
        self.keywordsEntry.bind("<Return>", lambda event: self.add_keyword())

        self.addKeywordButton = ttk.Button(
            self, text="Add Keyword", command=self.add_keyword)
        self.addKeywordButton.grid(row=0, column=2, sticky="ew")

        self.listbox = tkinter.Listbox(self)
        self.listbox.grid(row=1, column=0, columnspan=2, rowspan=4, sticky="nsew", padx=5)
        self.listbox.configure(width=40, height=25)
        self.populate_listbox()
        # Add a x amd y scrollbar to the listbox
        self.listview_xscrollbar = tkinter.Scrollbar(
            self.listbox, orient=tkinter.HORIZONTAL, command=self.listbox.xview)
        self.listview_xscrollbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        
        self.listview_yscrollbar = tkinter.Scrollbar(
            self.listbox, orient=tkinter.VERTICAL, command=self.listbox.yview)
        self.listview_yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.removeKeywordButton = ttk.Button(text="Remove keyword", command=self.remove_keyword)
        self.removeKeywordButton.grid(row=2, column=2, sticky="ew", pady=5)

        self.searchButton = ttk.Button(text="Search", command=lambda: bulkgoogle())
        self.searchButton.grid(row=3, column=2, sticky="ew", pady=5)

    def remove_keyword(self):
        # Get selected item
        selected = self.listbox.curselection()
        # Delete selected item from the bulkgoogling.txt file
        with open('./bulkgoogling.txt', 'r') as f:
            lines = f.readlines()
        with open('./bulkgoogling.txt', 'w') as f:
            for i, line in enumerate(lines):
                try:
                    if i != selected[0]:
                        f.write(line)
                except IndexError:
                    tkinter.messagebox.showerror(
                        "Error", "Please select a keyword to remove")

            f.close()
        # Repopulate the listbox
        self.populate_listbox()

    def create_layout(self):
        # Configure the grid rows and columns
        for r in range(5):
            self.grid_rowconfigure(r, weight=1)
        for c in range(3):
            self.grid_columnconfigure(c, weight=1)
        self.geometry("500x500")

    def add_keyword(self):
        if self.keywords.get().isspace() or self.keywords.get() == "":
            tkinter.messagebox.showerror(
                "Error", "Please enter keywords to search for", parent=self)
            return

        with open('./bulkgoogling.txt', 'a') as f:
            f.writelines([self.keywords.get()])
            f.write("\n")
            f.close()
        self.populate_listbox()

    def populate_listbox(self):
        # If the listbox is not empty or does not contain only spaces
        with open('./bulkgoogling.txt') as f:
            # Clear the listbox
            self.listbox.delete(0, tkinter.END)
            # Populate the listbox
            for line in f.readlines():
                self.listbox.insert(tkinter.END, line)
            f.close()
            
        # Clear the 
        self.keywords.set("")
    def search(self):
        with open('./bulkgoogling.txt', 'w') as f:
            f.write(self.textbox.get("1.0", "end-1c"))
            f.close()
        bulkgoogle()


if __name__ == "__main__":
    try:
        if sys.argv[1] in ["-c", "--console"]:
            is_console = True
        elif sys.argv[1] in ["-g", "--gui"]:
            is_console = False
    except IndexError:
        is_console = False
    finally:
        if is_console:
            bulkgoogle()
        else:
            try:
                app = MainFrame()
                app.mainloop()
            except Exception as e:
                print(e)
                tkinter.messagebox.showerror("Internal Error", traceback.format_exception(e))
                exit(1)
