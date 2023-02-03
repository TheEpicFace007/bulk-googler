import os
import time
import webbrowser
import urllib.parse
import tkinter
import sys

from rich import print

if not os.path.exists("./bulkgoogling.txt"):
    with open('./bulkgoogling.txt', 'w') as f:
        f.write('')
        print("./bulkgoogling.txt created, please add the keywords you want to search for in bulk")
        exit(0)
        

def google(keywords):
    webbrowser.open('https://www.google.com/search?q=' + urllib.parse.quote(keywords), 0, False)
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
        self.create_variables()
        self.create_widgets()
        self.create_layout()
    def create_variables(self):
        pass

    def search(self):
        with open('./bulkgoogling.txt', 'w') as f:
            f.write(self.textbox.get("1.0", "end-1c"))
        bulkgoogle()
        
if __name__ == "__main__":
    try:
        if sys.argv[1] in ["-c", "--console"]	:
            is_console = True
        elif sys.argv[1] in ["-g", "--gui"]:
            is_console = False
    except IndexError:
        is_console = False
    finally:
        if is_console:
            bulkgoogle()
        else:
            app = MainFrame()
            app.mainloop()