import os
import time
import webbrowser
import urllib.parse

from rich import print

if not os.path.exists("./bulkgoogling.txt"):
    with open('./bulkgoogling.txt', 'w') as f:
        f.write('')
        print("./bulkgoogling.txt created, please add the keywords you want to search for in bulk")
        exit(0)
        

def google(keywords):
    webbrowser.open('https://www.google.com/search?q=' + urllib.parse.quote(keywords), 0, False)
    time.sleep(0.05)
    
with open('./bulkgoogling.txt', 'r') as f:
    keywords = f.read().splitlines()
    for kw in keywords:
        print("[bold]Searching for[/bold] [underline]" + kw + "[/underline]")
        google(kw)