###############################################################################################################
#    klocks.py   Copyright (C) <2024>  <Kevin Scott>                                                            #
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

class MypyKlocksFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for the Application.

         Note : this frame uses a copy of the Config file i.e. not myConfig.
    """
    def __init__(self, master, main, Config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.Config     = Config
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.Config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Extra pyKlocks Settings", text_color=self.foreColour,
                                         fg_color=self.Config.BACKGROUND)
        self.lblTitle.grid(row=0, column=2)

        self.lblVFD = ctk.CTkLabel(self, text="VFD pyKlocks Settings", text_color=self.foreColour,
                                         fg_color=self.Config.BACKGROUND)
        self.lblVFD.grid(row=2, column=2)
        self.lblVFDForeColour = ctk.CTkLabel(self, text="Foreground Colour", text_color=self.foreColour,
                                          fg_color=self.Config.BACKGROUND)
        self.lblVFDForeColour.grid(row=3, column=0, padx=10, pady=10)
        self.btnVFDForeColour = ctk.CTkButton(self, text="Foreground Colour", command=self.__askVFDForeColour,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.Config.VFD_FOREGROUND, font=("Montserrat", 16))
        self.btnVFDForeColour.grid(row=3, column=1, padx=10, pady=10)

        self.lblVFDBackColour = ctk.CTkLabel(self, text="Background Colour", text_color=self.foreColour,
                                          fg_color=self.Config.BACKGROUND)
        self.lblVFDBackColour.grid(row=3, column=2, padx=10, pady=10)
        self.btnVFDBackColour = ctk.CTkButton(self, text="Background Colour", command=self.__askVFDBackColour,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnVFDBackColour.grid(row=3, column=3, padx=10, pady=10)

        self.lblText = ctk.CTkLabel(self, text="Text pyKlocks Settings", text_color=self.foreColour,
                                         fg_color=self.Config.BACKGROUND)
        self.lblText.grid(row=5, column=2)
        self.lblTextOnColour = ctk.CTkLabel(self, text="On Colour", text_color=self.foreColour,
                                          fg_color=self.Config.BACKGROUND)
        self.lblTextOnColour.grid(row=7, column=0, padx=10, pady=10)
        self.btnTextOnColour = ctk.CTkButton(self, text="On Colour", command=self.__askTextOnColour,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnTextOnColour.grid(row=7, column=1, padx=10, pady=10)

        self.lblTextOffColour = ctk.CTkLabel(self, text="Off Colour", text_color=self.foreColour,
                                          fg_color=self.Config.BACKGROUND)
        self.lblTextOffColour.grid(row=7, column=2, padx=10, pady=10)
        self.btnTextOffColour = ctk.CTkButton(self, text="Off Colour", command=self.__askTextOffColour,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnTextOffColour.grid(row=7, column=3, padx=10, pady=10)

        self.lblTextBackColour = ctk.CTkLabel(self, text="Background Colour", text_color=self.foreColour,
                                          fg_color=self.Config.BACKGROUND)
        self.lblTextBackColour.grid(row=8, column=2, padx=10, pady=10)
        self.btnTextBackColour = ctk.CTkButton(self, text="Background Colour", command=self.__askTextBackColour,
                                           fg_color="blue", hover_color="gray", corner_radius=12, width=100,
                                           text_color=self.foreColour, font=("Montserrat", 16))
        self.btnTextBackColour.grid(row=8, column=3, padx=10, pady=10)



    def __askVFDForeColour(self):
        """  Sets the forecolour of the VFD pyKlock - i.e. the text colour.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.Config.VFD_FOREGROUND = pickColor.get()                                    # get the colour string
        self.btnVFDForeColour.configure(text_color=self.Config.VFD_FOREGROUND)

    def __askVFDBackColour(self):
        """"  Sets the background of the VFD pyKlock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.Config.VFD_BACKGROUND = pickColor.get()                                    # get the colour string
        self.btnVFDBackColour.configure(text_color=self.Config.VFD_BACKGROUND)

    def __askTextOnColour(self):
        """  Sets the on colour of the letters in the text klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.Config.TEXTKLOCK_ON_COLOUR = pickColor.get()                               # get the colour string
        self.btnTextOnColour.configure(text_color=self.Config.TEXTKLOCK_ON_COLOUR)

    def __askTextOffColour(self):
        """  Sets the off colour of the letters in the text klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.Config.TEXTKLOCK_OFF_COLOUR = pickColor.get()                              # get the colour string
        self.btnTextOffColour.configure(text_color=self.Config.TEXTKLOCK_OFF_COLOUR)

    def __askTextBackColour(self):
        """  Sets the background colour of the text klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.Config.TEXTKLOCK_BACKGROUND = pickColor.get()                              # get the colour string
        self.btnTextBackColour.configure(text_color=self.Config.TEXTKLOCK_BACKGROUND)
