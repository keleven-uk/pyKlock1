###############################################################################################################
#    klocks.py   Copyright (C) <2024-25>  <Kevin Scott>                                                       #
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

class MyKlocksFrame(ctk.CTkFrame):
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
        self.lblTitle = ctk.CTkLabel(self, text="Extra Klocks Settings", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblTitle.grid(row=0, column=1)
        #---------------------------------------------------------------------------------------------- VFD klock -------------------------
        self.lblVFD = ctk.CTkLabel(self, text="VFD Klocks Settings", text_color="yellow", fg_color=self.config.BACKGROUND)
        self.lblVFD.grid(row=1, column=1)
        self.btnVFDForeColour = ctk.CTkButton(self, text="Foreground Colour", command=self.__askVFDForeColour, fg_color="blue",
                                              hover_color="gray", corner_radius=12, width=100, text_color=self.config.VFD_FOREGROUND,
                                              font=("Montserrat", 16))
        self.btnVFDForeColour.grid(row=2, column=0, padx=10, pady=10)
        self.btnVFDBackColour = ctk.CTkButton(self, text="Background Colour", command=self.__askVFDBackColour, fg_color="blue",
                                              hover_color="gray", corner_radius=12, width=100, text_color=self.config.VFD_BACKGROUND,
                                              font=("Montserrat", 16))
        self.btnVFDBackColour.grid(row=2, column=1, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- text klock -----------------------
        self.lblText = ctk.CTkLabel(self, text="Text Klocks Settings", text_color="yellow", fg_color=self.config.BACKGROUND)
        self.lblText.grid(row=3, column=1)
        self.btnTextOnColour = ctk.CTkButton(self, text="On Colour", command=self.__askTextOnColour, fg_color="blue", hover_color="gray",
                                             corner_radius=12, width=100, text_color=self.config.TEXTKLOCK_ON_COLOUR, font=("Montserrat", 16))
        self.btnTextOnColour.grid(row=4, column=0, padx=10, pady=10)
        self.btnTextOffColour = ctk.CTkButton(self, text="Off Colour", command=self.__askTextOffColour, fg_color="blue", hover_color="gray",
                                              corner_radius=12, width=100, text_color=self.config.TEXTKLOCK_OFF_COLOUR, font=("Montserrat", 16))
        self.btnTextOffColour.grid(row=4, column=1, padx=10, pady=10)
        self.btnTextBackColour = ctk.CTkButton(self, text="Background Colour", command=self.__askTextBackColour, fg_color="blue",
                                               hover_color="gray", corner_radius=12, width=100, text_color=self.config.TEXTKLOCK_BACKGROUND, font=("Montserrat", 16))
        self.btnTextBackColour.grid(row=4, column=2, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- dial klock -----------------------
        self.lblDial = ctk.CTkLabel(self, text="Dial Klocks Settings", text_color="yellow", fg_color=self.config.BACKGROUND)
        self.lblDial.grid(row=5, column=1)
        self.lblDialSize = ctk.CTkLabel(self, text="Dial Klock Size", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblDialSize.grid(row=6, column=0, padx=10, pady=10)
        self.entDialSize = ctk.CTkEntry(self, placeholder_text=self.config.DIALKLOCK_SIZE, width=50, text_color=self.foreColour,
                                        fg_color="#030126", border_color=self.foreColour, validate="focusout", validatecommand=(self.register(self.__validateSIze), "%P", "D"))
        self.entDialSize.grid(row=6, column=1,padx=10, pady=10)
        self.btnDialBackColour = ctk.CTkButton(self, text="Background Colour", command=self.__askDialBackColour, fg_color="blue",
                                               hover_color="gray", corner_radius=12, width=100, text_color=self.config.DIALKLOCK_BACKGROUND, font=("Montserrat", 16), border_color="white")
        self.btnDialBackColour.grid(row=7, column=0, padx=10, pady=10)
        self.btnDialTextColour = ctk.CTkButton(self, text="Text Colour", command=self.__askDialTextColour, fg_color="blue", hover_color="gray",
                                               corner_radius=12, width=100, text_color=self.config.DIALKLOCK_TEXT_COLOUR, font=("Montserrat", 16),
                                               border_color=self.foreColour)
        self.btnDialTextColour.grid(row=7, column=1, padx=10, pady=10)
        self.btnDialScaleColour = ctk.CTkButton(self, text="Scale Colour", command=self.__askDialScaleColour, fg_color="blue", hover_color="gray",
                                                corner_radius=12, width=100, text_color=self.config.DIALKLOCK_SCALE_COLOUR, font=("Montserrat", 16),
                                                border_color=self.foreColour)
        self.btnDialScaleColour.grid(row=7, column=2, padx=10, pady=10)
        self.btnDialNeedleColour = ctk.CTkButton(self, text="Needle Colour", command=self.__askDialNeedleColour, fg_color="blue", hover_color="gray",
                                                 corner_radius=12, width=100, text_color=self.config.DIALKLOCK_NEEDLE_COLOUR, font=("Montserrat", 16),
                                                 border_color=self.foreColour)
        self.btnDialNeedleColour.grid(row=7, column=3, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- binary klock -----------------------
        self.lblDial = ctk.CTkLabel(self, text="Binary Klocks Settings", text_color="yellow", fg_color=self.config.BACKGROUND)
        self.lblDial.grid(row=8, column=1)
        self.lblBinarySize = ctk.CTkLabel(self, text="Binary Klock Size", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblBinarySize.grid(row=9, column=0, padx=10, pady=10)
        self.entBinarySize = ctk.CTkEntry(self, placeholder_text=self.config.BINARYKLOCK_SIZE, width=50, text_color=self.foreColour,
                                          fg_color="#030126", border_color=self.foreColour, validate="focusout", validatecommand=(self.register(self.__validateSIze), "%P", "B"))
        self.entBinarySize.grid(row=9, column=1,padx=10, pady=10)


    def __validateSIze(self, data, type):
        """  Size has to be an integer number.
             The validation checks this and only allows decimal numbers.
             This is called by all three stage days entry fields.
        """
        valid = data.isdecimal()

        if valid:
            self.master.btnSave.configure(state="normal")
            match type:
                case "D":
                    self.config.DIALKLOCK_SIZE = int(data)
                case "B":
                    self.config.BINARYKLOCK_SIZE = int(data)

        return valid

    def __askDialNeedleColour(self):
        """  Sets the background colour of the Dial Klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                      # open the colour picker
        self.config.DIALKLOCK_NEEDLE_COLOUR = pickColor.get()                              # get the colour string
        self.btnDialNeedleColour.configure(text_color=self.config.DIALKLOCK_NEEDLE_COLOUR)

    def __askDialScaleColour(self):
        """  Sets the background colour of the Dial Klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                     # open the colour picker
        self.config.DIALKLOCK_SCALE_COLOUR = pickColor.get()                              # get the colour string
        self.btnDialScaleColour.configure(text_color=self.config.DIALKLOCK_SCALE_COLOUR)


    def __askDialBackColour(self):
        """  Sets the background colour of the Dial Klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.DIALKLOCK_BACKGROUND = pickColor.get()                              # get the colour string
        self.btnDialBackColour.configure(text_color=self.config.DIALKLOCK_BACKGROUND)

    def __askDialTextColour(self):
        """  Sets the text colour of the Dial Klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.DIALKLOCK_TEXT_COLOUR = pickColor.get()                             # get the colour string
        self.btnDialTextColour.configure(text_color=self.config.DIALKLOCK_TEXT_COLOUR)

    def __askVFDForeColour(self):
        """  Sets the forecolour of the VFD pyKlock - i.e. the text colour.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.VFD_FOREGROUND = pickColor.get()                                    # get the colour string
        self.btnVFDForeColour.configure(text_color=self.config.VFD_FOREGROUND)

    def __askVFDBackColour(self):
        """"  Sets the background of the VFD pyKlock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.VFD_BACKGROUND = pickColor.get()                                    # get the colour string
        self.btnVFDBackColour.configure(text_color=self.config.VFD_BACKGROUND)

    def __askTextOnColour(self):
        """  Sets the on colour of the letters in the text klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.TEXTKLOCK_ON_COLOUR = pickColor.get()                               # get the colour string
        self.btnTextOnColour.configure(text_color=self.config.TEXTKLOCK_ON_COLOUR)

    def __askTextOffColour(self):
        """  Sets the off colour of the letters in the text klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.TEXTKLOCK_OFF_COLOUR = pickColor.get()                              # get the colour string
        self.btnTextOffColour.configure(text_color=self.config.TEXTKLOCK_OFF_COLOUR)

    def __askTextBackColour(self):
        """  Sets the background colour of the text klock.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                   # open the colour picker
        self.config.TEXTKLOCK_BACKGROUND = pickColor.get()                              # get the colour string
        self.btnTextBackColour.configure(text_color=self.config.TEXTKLOCK_BACKGROUND)
