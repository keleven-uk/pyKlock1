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


class ColourWindow(ctk.CTkToplevel):
    """  A class for choosing colours.
         An external colour picker is launched for the user to select colours.

    """
    def __init__(self, master, myConfig):
        super().__init__(master)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Colour Chooser")
        self.myConfig = myConfig
        self.geometry("400x200+400+600")
        self.resizable(False, False)

        self.foreColour = ""
        self.backColour = ""

        self._create_widgets()


    def _create_widgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color="black")
        self.lblTitle = ctk.CTkLabel(master=self, text="Click on required button to set the colour.", fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.lblTitle.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), columnspan=3)

        self.btnForeColour = ctk.CTkButton(self, text="Foreground Colour", command=self._askForeColour, fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.btnForeColour.grid(row=1, column=0, padx=(0, 0), pady=(20, 20))

        self.btnBackColour = ctk.CTkButton(self, text="Background Colour", command=self._askBackColour, fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.btnBackColour.grid(row=1, column=1, padx=(0, 0), pady=(20, 20))

        self.btnApply = ctk.CTkButton(self, text="Apply", command=self._applyInfo, fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.btnApply.grid(row=2, column=0, padx=(0, 0), pady=(20, 20))

        self.btnReset = ctk.CTkButton(self, text="Reset", command=self._resetInfo, fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.btnReset.grid(row=2, column=1, padx=(0, 0), pady=(20, 20))

        self.btnCancel = ctk.CTkButton(self, text="Cancel", command=self._cancel, fg_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND)
        self.btnCancel.grid(row=2, column=2, padx=(0, 0), pady=(20, 20))


    def _cancel(self):
        """  Closes the window.
        """
        self.destroy()


    def _resetInfo(self):
        """  Rested the foreground colour to green and the background colour to black.
        """
        self.foreColour = "#00ff00"
        self.lblTitle.configure(text_color=self.foreColour)
        self.btnForeColour.configure(text_color=self.foreColour)
        self.btnBackColour.configure(text_color=self.foreColour)
        self.btnApply.configure(text_color=self.foreColour)
        self.btnReset.configure(text_color=self.foreColour)
        self.btnCancel.configure(text_color=self.foreColour)
        self.backColour = "#000000"
        self.lblTitle.configure(fg_color=self.backColour)
        self.btnForeColour.configure(fg_color=self.backColour)
        self.btnBackColour.configure(fg_color=self.backColour)
        self.btnApply.configure(fg_color=self.backColour)
        self.btnReset.configure(fg_color=self.backColour)
        self.btnCancel.configure(fg_color=self.backColour)


    def _applyInfo(self):
        """  Apply the selected colours by amended to config file.
        """
        if self.foreColour:
            self.myConfig.FOREGROUND = self.foreColour
        if self.backColour:
            self.myConfig.BACKGROUND = self.backColour


    def _askForeColour(self):
        """  Ask the user to select a new foreground colour.
        """
        pickColor = ctk_cp.AskColor() # open the colour picker
        self.foreColour = pickColor.get() # get the colour string
        self.btnForeColour.configure(text_color=self.foreColour)
        self.btnBackColour.configure(text_color=self.foreColour)

    def _askBackColour(self):
        """  Ask the user to select a new background colour.
        """
        pickColor = ctk_cp.AskColor() # open the colour picker
        self.backColour = pickColor.get() # get the colour string
        self.btnForeColour.configure(fg_color=self.backColour)
        self.btnBackColour.configure(fg_color=self.backColour)
