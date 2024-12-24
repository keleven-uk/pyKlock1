###############################################################################################################
#    font.py   Copyright (C) <2024>  <Kevin Scott>                                                            #
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

         Note : this frame uses a copy of the Config file i.e. not myConfig.
    """
    def __init__(self, master, main, Config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.Config   = Config
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.Config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Font Settings", text_color=self.foreColour,
                                         fg_color=self.Config.BACKGROUND)
        self.lblTitle.grid(row=0, column=2)
        self.lblTimeFont = ctk.CTkLabel(self, text="Main Time Font", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblTimeFont.grid(row=1, column=0, padx=10, pady=10)
        self.btnTimeFont = ctk.CTkButton(self, text="Time Font", command=self.__askTimeFont,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnTimeFont.grid(row=1, column=1, padx=10, pady=10)
        timeFont = f"    Main Time Font Family {self.Config.TIME_FONT_FAMILY} with size {self.Config.TIME_FONT_SIZE}"
        self.lblCurrTime = ctk.CTkLabel(self, text=timeFont, text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblCurrTime.grid(row=1, column=2)

        self.lblStatusFont = ctk.CTkLabel(self, text="Status Bar Font", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblStatusFont.grid(row=2, column=0, padx=10, pady=10)
        self.btnStatusFont = ctk.CTkButton(self, text="Time Font", command=self.__askStatusFont,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnStatusFont.grid(row=2, column=1, padx=10, pady=10)
        statusFont = f"    Main Time Font Family {self.Config.STATUS_FONT_FAMILY} with size {self.Config.STATUS_FONT_SIZE}"
        self.lblCurrStatus = ctk.CTkLabel(self, text=statusFont, text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblCurrStatus.grid(row=2, column=2)


    def __askTimeFont(self):
        """  Sets the font for the main text display.
        """
        self.master.btnSave.configure(state="normal")
        font = askfont(self)
        #font is "" if the user has cancelled
        if font:
            self.Config.TIME_FONT_FAMILY = font["family"]
            self.Config.TIME_FONT_SIZE   = font["size"]

    def __askStatusFont(self):
        """  Sets the font for the status bar.
        """
        self.master.btnSave.configure(state="normal")
        font = askfont(self)
        # font is "" if the user has cancelled
        if font:
            self.Config.STATUS_FONT_FAMILY = font["family"]
            self.Config.STATUS_FONT_SIZE   = font["size"]
