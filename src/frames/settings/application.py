###############################################################################################################
#    application.py   Copyright (C) <2024>  <Kevin Scott>                                                     #
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

import CTkColorPicker as ctk_cp

class MyApplicationFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for the Application.
    """
    def __init__(self, master, main, myConfig):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.myConfig   = myConfig
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Application Settings", text_color=self.foreColour,
                                         fg_color=self.myConfig.BACKGROUND)
        self.lblTitle.grid(row=0, column=3)

        self.lblAppearanceMode = ctk.CTkLabel(self, text="Appearance Mode", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblAppearanceMode.grid(row=1, column=0, padx=10, pady=10)
        self.cbxAppearanceMode = ctk.CTkComboBox(self, values=self.myConfig.APPEARANCE_MODE_TYPES, text_color="white",
                                                 fg_color="#030126", border_color="#030126", command=self.__setAppearanceMode)
        self.cbxAppearanceMode.grid(row=1, column=1, padx=10, pady=10)
        self.cbxAppearanceMode.set(self.myConfig.APPEARANCE_MODE)

        self.lblColorThemeMode = ctk.CTkLabel(self, text="Color Theme", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblColorThemeMode.grid(row=1, column=2, padx=10, pady=10)
        self.cbxColorThemeMode = ctk.CTkComboBox(self, values=self.myConfig.COLOR_THEME_TYPES, text_color="white",
                                                 fg_color="#030126", border_color="#030126", command=self.__setcolorThemeTypes)
        self.cbxColorThemeMode.grid(row=1, column=3, padx=10, pady=10)
        self.cbxColorThemeMode.set(self.myConfig.COLOR_THEME)

        self.lblTransparent = ctk.CTkLabel(self, text="Background Transparent", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblTransparent.grid(row=2, column=0, padx=10, pady=10)
        self.chkTransparent = ctk.CTkCheckBox(self, text="", fg_color="#030126", border_color=self.foreColour,
                                              hover_color="gray", command=self.__setTransparent)
        self.chkTransparent.grid(row=2, column=1, padx=10, pady=10)
        if self.myConfig.TRANSPARENT:
            self.chkTransparent.select()
        else:
            self.chkTransparent.deselect()

        self.lblAlighnRight = ctk.CTkLabel(self, text="Right Align Klock", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblAlighnRight.grid(row=2, column=2, padx=10, pady=10)
        self.chkAlighnRight = ctk.CTkCheckBox(self, text="", fg_color="#030126", border_color=self.foreColour,
                                              hover_color="gray", command=self.__setAlighnRight)
        self.chkAlighnRight.grid(row=2, column=3, padx=10, pady=10)
        if self.myConfig.ALIGN_RIGHT:
            self.chkAlighnRight.select()
        else:
            self.chkAlighnRight.deselect()

        self.lblForeColour = ctk.CTkLabel(self, text="Foreground Colour", text_color=self.foreColour,
                                          fg_color=self.myConfig.BACKGROUND)
        self.lblForeColour.grid(row=3, column=0, padx=10, pady=10)
        self.btnForeColour = ctk.CTkButton(self, text="Foreground Colour", command=self.__askForeColour,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnForeColour.grid(row=3, column=1, padx=10, pady=10)

        self.lblBackColour = ctk.CTkLabel(self, text="Background Colour", text_color=self.foreColour,
                                          fg_color=self.myConfig.BACKGROUND)
        self.lblBackColour.grid(row=3, column=2, padx=10, pady=10)
        self.btnBackColour = ctk.CTkButton(self, text="Background Colour", command=self.__askForeColour,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnBackColour.grid(row=3, column=3, padx=10, pady=10)


    def __setAppearanceMode(self, choice):
        pass

    def __setcolorThemeTypes(self, choice):
        pass

    def __setTransparent(self):
        self.master.btnSave.configure(state="normal")

    def __setAlighnRight(self):
        pass

    def __askForeColour(self):
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor() # open the colour picker

    def __askBackColour(sefl):
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor() # open the colour picker

