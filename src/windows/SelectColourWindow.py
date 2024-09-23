###############################################################################################################
#    SelectColourWindow.py   Copyright (C) <2024>  <Kevin Scott>                                              #
#    For changes see history.txt                                                                              #
#                                                                                                             #
#    Colour picker used is from https://github.com/Akascape/CTkColorPicker.                                   #
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
import CTkColorPicker as ctk_cp

import src.config as Config

from src.projectPaths import LOGGER_PATH, CONFIG_PATH

class ColourWindow(ctk.CTkToplevel):
    def __init__(self, master, myConfig):
        super().__init__(master)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.myConfig = myConfig
        self.geometry("400x200+400+400")
        self.resizable(False, False)

        self.foreColour = ""
        self.backColour = ""

        self.create_widgets()


    def create_widgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color="black")
        self.lblTitle = ctk.CTkLabel(master=self, text="Click on required button to set the colour.", fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.lblTitle.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), columnspan=2)

        self.btnForeColour = ctk.CTkButton(self, text="Foreground Colour", command=self.askForeColour, fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.btnForeColour.grid(row=1, column=0, padx=(20, 20), pady=(20, 20))

        self.btnBackColour = ctk.CTkButton(self, text="Background Colour", command=self.askBackColour, fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.btnBackColour.grid(row=1, column=1, padx=(20, 20), pady=(20, 20))

        self.sbMenu = ctk.CTkSegmentedButton(self, values=["Apply", "Reset", "Cancel"],
                                             command=self.callback, unselected_color=self.myConfig.BACKGROUND,
                                             text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.sbMenu .grid(row=2, column=0, padx=(20, 20), columnspan=2)


    def callback(self, value):
        match value:
            case "Apply":
                self.applyInfo()
            case "Save":
                self.saveInfo()
            case "Reset":
                self.resetInfo()
            case "Cancel":
                self.cancel()


    def cancel(self):
        self.destroy()


    def resetInfo(self):
        print("resetInfo")
        self.foreColour = "#00ff00"
        self.lblTitle.configure(text_color=self.foreColour)
        self.btnForeColour.configure(text_color=self.foreColour)
        self.btnBackColour.configure(text_color=self.foreColour)
        self.sbMenu.configure(text_color=self.foreColour)
        self.backColour = "#000000"
        self.lblTitle.configure(fg_color=self.backColour)
        self.btnForeColour.configure(fg_color=self.backColour)
        self.btnBackColour.configure(fg_color=self.backColour)
        self.sbMenu.configure(fg_color=self.backColour)


    def applyInfo(self):
        if self.foreColour:
            self.myConfig.FOREGROUND = self.foreColour
        if self.backColour:
            self.myConfig.BACKGROUND = self.backColour


    def askForeColour(self):
        pickColor = ctk_cp.AskColor() # open the color picker
        self.foreColour = pickColor.get() # get the color string
        self.btnForeColour.configure(text_color=self.foreColour)
        self.btnBackColour.configure(text_color=self.foreColour)

    def askBackColour(self):
        pickColor = ctk_cp.AskColor() # open the color picker
        self.backColour = pickColor.get() # get the color string
        self.btnForeColour.configure(fg_color=self.backColour)
        self.btnBackColour.configure(fg_color=self.backColour)
