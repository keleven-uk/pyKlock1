pyKlock.

Previous versions of Klock have existed in VB.net, Lazarus [Free Pascal] and Free Basic - and may again.

Current version of Klock is written in Python using different GUI frameworks

    Klock 0 - pygubu & pySimpleGUI - finally settled on pySimpleGUI.  Most complete.
    Klock 1 - CustomTkinter - this one
    Klock 2 - Flet.
    
    Note : pySimpleGUI is licensed software product, but free for hobbyist [but need to register]

<img src="resources\Klock.jpg" title="Klock Display" alt="" data-align="center">

A klock built using Python and CuistomTKinter.

Using python 3.12.7 and CustonTKinter 5.2.2.

Note : I use the correct spelling of colour on my side of the code.  :-)

Klock displays the time [local], date, key status and the computers idle time.
Key status is the status of Caps Lock, Insert, Scroll lock and Num lock.
The format of the time display can be changes i.e GMT, UTC, in words, numbers and the famous Fuzzy Time.

Klock will store a number of friends [contacts] that are display in a table.
Each friend can be edited and deleted.

The foreground and background colours can be selected.

Klock is moved by dragging the displayed time.

Klock currently has a transparent background.

Klock should remain on top of other other windows.

To install dependencies pip install -r requirements.txt

To install all dependencies pip install -r requirements.txt - r requirements_dev.txt

-     [needed mainly for pyinstaller & auto-py-to-exe.exe]

For changes see history.txt

Kevin Scott (C) 2024 :: pyKlock V2024.31
