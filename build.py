import pyshortcuts
import os


pyshortcuts.make_shortcut(
    script='bulkgoogle.py',
    icon='icon',
    working_dir=os.getcwd(),
    name='Bulk Googler',
    desktop=True,
    startmenu=True,
    terminal=False,
)
print("Shortcut created successfully")
