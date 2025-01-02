pyKlock - a clock with a k.

A multifunction timing thingy, where some [but not necessary all] of the things are useful.

pyKlock serves as a vehicle by which I learn and tinker with programming.

Previous versions of pyKlock have existed in VB.net, Lazarus [Free Pascal] and Free Basic - and may again.

Current version of pyKlock is written in Python using different GUI frameworks

    pyKlock 0 - pygubu & pySimpleGUI - finally settled on pySimpleGUI.  Most complete.
    pyKlock 1 - CustomTkinter - this one
    pyKlock 2 - Flet.

    Note : pySimpleGUI is licensed software product, but free for hobbyist [but need to register]

<img src="resources\pyKlock.jpg" title="pyKlock Display" alt="" data-align="center">

A klock built using Python and CuistomTKinter.

Using python 3.12.8 and CustonTKinter 5.2.2.

Note : I use the correct spelling of colour on my side of the code.  :-)

pyKlock displays the time [local], date, key status and the computers idle time.
Key status is the status of Caps Lock, Insert, Scroll lock and Num lock.
The format of the time display can be changes i.e GMT, UTC, in words, numbers and the famous Fuzzy Time.

pyKlock will store a number of friends [contacts] that are displayed in a table.
Each friend can be edited and deleted.

pyKlock will store a number of events that are displayed in a table.
These events have a date due attached to them, pyKlock will give notifications when up and coming.

Added sound to pyKlock.
	pyKlock can play Westminster type chimes on the quarter, half and on the hour.
	pyKlock can also imitate a Cuckoo pyKlock.
	pyKlock can also play "the pips" on the hour.

The foreground and background colours can be selected.

pyKlock is moved by dragging the displayed time.

pyKlock currently has a transparent background.

pyKlock should remain on top of other other windows.

To install dependencies pip install -r requirements.txt

To install all dependencies pip install -r requirements.txt - r requirements_dev.txt

-     [needed mainly for pyinstaller & auto-py-to-exe.exe]

For changes see history.txt

Kevin Scott (C) 2024-25 :: pyKlock V2025.58
