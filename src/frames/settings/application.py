###############################################################################################################
#    application.py   Copyright (C) <2024-25>  <Kevin Scott>                                                  #
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

         Note : this frame uses a copy of the config file i.e. not config.
    """
    def __init__(self, master, main, config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.config     = config
        self.foreColour = "white"

        self.__createWidgets()
        self.__setWidgets()

    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Application Settings", text_color="yellow",
                                         fg_color=self.config.BACKGROUND)
        self.lblTitle.grid(row=0, column=2)
        #---------------------------------------------------------------------------------------------- Appearance Mode ------------------
        self.lblAppearanceMode = ctk.CTkLabel(self, text="Appearance Mode", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblAppearanceMode.grid(row=1, column=0, padx=10, pady=10)
        self.cbxAppearanceMode = ctk.CTkComboBox(self, values=self.config.APPEARANCE_MODE_TYPES, text_color=self.foreColour,
                                                 fg_color="#030126", border_color="#030126", command=self.__setAppearanceMode)
        self.cbxAppearanceMode.grid(row=1, column=1, padx=10, pady=10)
        self.cbxAppearanceMode.set(self.config.APPEARANCE_MODE)
        #---------------------------------------------------------------------------------------------- Colour Theme ---------------------
        self.lblColorThemeMode = ctk.CTkLabel(self, text="Color Theme", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblColorThemeMode.grid(row=1, column=2, padx=10, pady=10)
        self.cbxColorThemeMode = ctk.CTkComboBox(self, values=self.config.COLOUR_THEME_TYPES, text_color=self.foreColour,
                                                 fg_color="#030126", border_color="#030126", command=self.__setColourThemeTypes)
        self.cbxColorThemeMode.grid(row=1, column=3, padx=10, pady=10)
        self.cbxColorThemeMode.set(self.config.COLOUR_THEME)
        #---------------------------------------------------------------------------------------------- Background Transparent -----------
        self.lblTransparent = ctk.CTkLabel(self, text="Background Transparent", text_color=self.foreColour,
                                           fg_color=self.config.BACKGROUND)
        self.lblTransparent.grid(row=2, column=0, padx=10, pady=10)
        self.chkTransparent = ctk.CTkCheckBox(self, text="", fg_color="#030126", border_color=self.foreColour, hover_color="gray",
                                              command=self.__setTransparent)
        self.chkTransparent.grid(row=2, column=1, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Right Align pyKlock --------------
        self.lblAlighnRight = ctk.CTkLabel(self, text="Right Align pyKlock", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblAlighnRight.grid(row=2, column=2, padx=10, pady=10)
        self.chkAlighnRight = ctk.CTkCheckBox(self, text="", fg_color="#030126", border_color=self.foreColour, hover_color="gray",
                                              command=self.__setAlighnRight)
        self.chkAlighnRight.grid(row=2, column=3, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Foreground Colour ----------------
        self.btnForeColour = ctk.CTkButton(self, text="Foreground Colour", command=self.__askForeColour, fg_color="blue",
                                           hover_color="gray", corner_radius=12, width=100, text_color=self.config.FOREGROUND,
                                           font=("Montserrat", 16))
        self.btnForeColour.grid(row=3, column=0, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Background Colour ----------------
        self.btnBackColour = ctk.CTkButton(self, text="Background Colour", command=self.__askForeColour, fg_color="blue",
                                           hover_color="gray", corner_radius=12, width=100, text_color=self.config.BACKGROUND,
                                           font=("Montserrat", 16))
        self.btnBackColour.grid(row=3, column=1, padx=10, pady=10)


    def __setWidgets(self):
        """  Sets initial state of the widgets.
        """
        if self.config.TRANSPARENT:
            self.chkTransparent.select()
        else:
            self.chkTransparent.deselect()

        if self.config.ALIGN_RIGHT:
            self.chkAlighnRight.select()
        else:
            self.chkAlighnRight.deselect()

    def __setAppearanceMode(self, choice):
        """  A new Appearance Mode has been selected.
             Enable the save button in the parent window and amend the config file with then new time type.
        """
        self.master.btnSave.configure(state="normal")
        self.config.APPEARANCE_MODE = choice

    def __setColourThemeTypes(self, choice):
        """  A new Colour Theme has been selected.
             Enable the save button in the parent window and amend the config file with then new time type.
        """
        self.master.btnSave.configure(state="normal")
        self.config.COLOUR_THEME = choice

    def __setTransparent(self):
        """  Set if pyKlock has a Transparent background.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkTransparent.get()
        self.config.TRANSPARENT = True if clicked == 1 else False

    def __setAlighnRight(self):
        """  Set if pyKlock has is aligned with the right side of the monitor.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkAlighnRight.get()
        self.config.ALIGN_RIGHT = True if clicked == 1 else False

    def __askForeColour(self):
        """  Sets the forecolour of pyKlock - i.e. the text colour.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.FOREGROUND = pickColor.get()                                        # get the colour string
        self.btnForeColour.configure(text_color=self.config.FOREGROUND)

    def __askBackColour(self):
        """  Sets the back colour of pyKlock - i.e. the text colour.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.BACKGROUND = pickColor.get()                                        # get the colour string
        self.btnBackColour.configure(text_color=self.config.BACKGROUND)

