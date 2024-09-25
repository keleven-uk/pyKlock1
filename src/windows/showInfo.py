###############################################################################################################
#    showInfo.py   Copyright (C) <2024>  <Kevin Scott>                                                        #
#    For changes see history.txt                                                                              #
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

import customtkinter as ctk

from src.projectPaths import HISTORY_PATH, LICENSE_PATH

class showInfo(ctk.CTkToplevel):
    """  A class to display the contents of a text file on a new top level window.
         The text file is displayed in a text box that fill the entire window.
         The X in the top right corner is used to close the window.
    """
    def __init__(self, master, infoType):
        super().__init__(master)

        self.infoType = infoType

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("1000x800+200+200")
        self.resizable(False, False)

        self.infoText = f"{self.infoType} Not Found"
        self._loadInfo()

        self._create_widgets()


    def _create_widgets(self):
        """  Create the history display display.
        """
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = ctk.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", self.infoText)


    def _loadInfo(self):
        """  Loads the info file.  The type of info file is held in self.infoText
             If the file is not present, the initial string is set to "Info Not Found",
             so we can ignore exceptions - can we?
        """
        match self.infoType:
            case "History":
                self.infoText = HISTORY_PATH.read_text()
            case "License":
                self.infoText = LICENSE_PATH.read_text()



