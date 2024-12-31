###############################################################################################################
#    showSettings.py   Copyright (C) <2024>  <Kevin Scott>                                                    #
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

import src.frames.showpyKlockSettings as pyKlockSettings

class showSettings(ctk.CTkToplevel):
    """  A class to display pyKlock's help file in pdf format.
    """
    def __init__(self, master, myConfig, myLogger):
        super().__init__(master)

        self.myConfig = myConfig
        self.myLogger      = myLogger

        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)
        ctk.set_default_color_theme(self.myConfig.COLOUR_THEME)

        self.geometry("700x500")
        self.title("pyKlock Settings")
        self.resizable(False, False)

        #  Create the frame for the main time text.
        self.settings = pyKlockSettings.MySettings(self, self.myConfig, self.myLogger)
        self.settings.pack(expand=True)
