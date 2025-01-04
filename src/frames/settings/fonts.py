###############################################################################################################
#    fonts.py   Copyright (C) <2024-25>  <Kevin Scott>                                                        #
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

from tkfontchooser import askfont

class MyFontFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for the Application.

         Note : this frame uses a copy of the config file i.e. not myconfig.
    """
    def __init__(self, master, main, config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.config     = config
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Font Settings", text_color="yellow", fg_color=self.config.BACKGROUND)
        self.lblTitle.grid(row=0, column=1)
        #---------------------------------------------------------------------------------------------- Main Time Font ---------------
        self.btnTimeFont = ctk.CTkButton(self, text="Main Time Font", command=self.__askTimeFont, fg_color="blue", hover_color="gray",
                                         corner_radius=12, width=100, text_color=self.foreColour, font=("Montserrat", 16))
        self.btnTimeFont.grid(row=1, column=0, padx=10, pady=10)
        timeFont = f"    Main Time Font Family {self.config.TIME_FONT_FAMILY} with size {self.config.TIME_FONT_SIZE}"
        self.lblCurrTime = ctk.CTkLabel(self, text=timeFont, text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblCurrTime.grid(row=1, column=1)
        #---------------------------------------------------------------------------------------------- Status Bar Font ---------------
        self.btnStatusFont = ctk.CTkButton(self, text="Status Bar Font", command=self.__askStatusFont, fg_color="blue",
                                           hover_color="gray", corner_radius=12, width=100, text_color=self.foreColour,
                                           font=("Montserrat", 16))
        self.btnStatusFont.grid(row=2, column=0, padx=10, pady=10)
        statusFont = f"    Main Time Font Family {self.config.STATUS_FONT_FAMILY} with size {self.config.STATUS_FONT_SIZE}"
        self.lblCurrStatus = ctk.CTkLabel(self, text=statusFont, text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblCurrStatus.grid(row=2, column=1)

    def __askTimeFont(self):
        """  Sets the font for the main text display.
        """
        self.master.btnSave.configure(state="normal")
        font = askfont(self)
        #font is "" if the user has cancelled
        if font:
            self.config.TIME_FONT_FAMILY = font["family"]
            self.config.TIME_FONT_SIZE   = font["size"]

    def __askStatusFont(self):
        """  Sets the font for the status bar.
        """
        self.master.btnSave.configure(state="normal")
        font = askfont(self)
        # font is "" if the user has cancelled
        if font:
            self.config.STATUS_FONT_FAMILY = font["family"]
            self.config.STATUS_FONT_SIZE   = font["size"]
