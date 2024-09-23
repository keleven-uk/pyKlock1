###############################################################################################################
#    SelectColourWindow.py   Copyright (C) <2024>  <Kevin Scott>                                              #
#    For changes see history.txt                                                                              #
#                                                                                                             #
#    Menu used is from https://github.com/Akascape/CTkMenuBar.                                                #
#                                                                                                             #
###############################################################################################################
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################


from CTkMenuBar import *


class myMenu(CTkMenuBar):

        def __init__(self, master):
            super().__init__(master)

            menu = CTkMenuBar(master)
            button_1 = menu.add_cascade("File")
            button_2 = menu.add_cascade("Edit")
            button_3 = menu.add_cascade("Settings")
            button_4 = menu.add_cascade("About")

            dropdown1 = CustomDropdownMenu(widget=button_1)
            dropdown1.add_option(option="Open", command=lambda: print("Open"))
            dropdown1.add_option(option="Save")

            dropdown1.add_separator()

            sub_menu = dropdown1.add_submenu("Export As")
            sub_menu.add_option(option=".TXT")
            sub_menu.add_option(option=".PDF")

            dropdown2 = CustomDropdownMenu(widget=button_2)
            dropdown2.add_option(option="Cut")
            dropdown2.add_option(option="Copy")
            dropdown2.add_option(option="Paste")

            dropdown3 = CustomDropdownMenu(widget=button_3)
            dropdown3.add_option(option="Preferences")
            dropdown3.add_option(option="Update")

            dropdown4 = CustomDropdownMenu(widget=button_4)
            dropdown4.add_option(option="Hello World")

            button_1.configure(text_color="green")

