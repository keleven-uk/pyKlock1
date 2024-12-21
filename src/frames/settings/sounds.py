###############################################################################################################
#    sounds.py   Copyright (C) <2024>  <Kevin Scott>                                                          #
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

class MySoundFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for the Application.
    """
    def __init__(self, master, main, myConfig):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.myConfig   = myConfig
        self.foreColour = "white"

        self.__createWidgets()
        self.__setWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Sound Settings", text_color=self.foreColour,
                                         fg_color=self.myConfig.BACKGROUND)
        self.lblTitle.grid(row=0, column=2)
        self.lblSound = ctk.CTkLabel(self, text="Sound Enabled", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblSound.grid(row=1, column=0, padx=10, pady=10)
        self.chkSound = ctk.CTkCheckBox(self, text="", fg_color=self.myConfig.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__setSound)
        self.chkSound.grid(row=1, column=1, padx=10, pady=10)
        self.lblHrChimes = ctk.CTkLabel(self, text="Hour Chimes", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblHrChimes.grid(row=2, column=0, padx=10, pady=10)
        self.chkHrChimes = ctk.CTkCheckBox(self, text="", fg_color=self.myConfig.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__hourChimes)
        self.chkHrChimes.grid(row=2, column=1, padx=10, pady=10)
        self.lblQtrChimes = ctk.CTkLabel(self, text="Quarter Hour Chimes", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblQtrChimes.grid(row=2, column=2, padx=10, pady=10)
        self.chkQtrChimes = ctk.CTkCheckBox(self, text="", fg_color=self.myConfig.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__qtrHourChimes)
        self.chkQtrChimes.grid(row=2, column=3, padx=10, pady=10)
        self.lblPips = ctk.CTkLabel(self, text="The Pips on the Hour", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblPips.grid(row=3, column=0, padx=10, pady=10)
        self.chkPips = ctk.CTkCheckBox(self, text="", fg_color=self.myConfig.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__pips)
        self.chkPips.grid(row=3, column=1, padx=10, pady=10)
        self.lblVolume = ctk.CTkLabel(self, text="Sound Volume", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblVolume.grid(row=4, column=0, padx=10, pady=10)
        self.sldVolume= ctk.CTkSlider(self, from_=0, to=50, command=self.__soundVolume)
        self.sldVolume.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
        self.lblCurVol = ctk.CTkLabel(self, text=f"Current Volume {self.myConfig.SOUND_VOLUME}", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblCurVol.grid(row=4, column=3, padx=10, pady=10)

    def __setSound(self):
        self.master.btnSave.configure(state="normal")

        if self.chkSound.get():
            print("on")
            self.__switchOnSounds()
        else:
            print("off")
            self.__switchOffSounds()

    def __hourChimes(self):
        self.master.btnSave.configure(state="normal")

    def __qtrHourChimes(self):
        self.master.btnSave.configure(state="normal")

    def __pips(self):
        self.master.btnSave.configure(state="normal")

    def __soundVolume(self, choice):
        self.master.btnSave.configure(state="normal")
        self.lblCurVol.configure(text=f"Current Volume {self.sldVolume.get():0.0f}")

    def __setWidgets(self):
        if self.myConfig.SOUNDS:
            self.chkSound.select()
            self.__switchOnSounds()
        else:
            self.chkSound.deselect()
            self.__switchOffSounds()

    def __switchOnSounds(self):
        self.chkHrChimes.configure(state="normal")
        self.chkQtrChimes.configure(state="normal")
        self.chkPips.configure(state="normal")
        self.sldVolume.configure(state="normal")
        self.sldVolume.set(self.myConfig.SOUND_VOLUME)
        self.sldVolume.configure(number_of_steps=50)

        if self.myConfig.SOUNDS_HOUR_CHIMES:
            self.chkHrChimes.select()
        else:
            self.chkHrChimes.deselect()

        if self.myConfig.SOUNDS_QUARTER_CHIMES:
            self.chkQtrChimes.select()
        else:
            self.chkQtrChimes.deselect()

        if self.myConfig.SOUNDS_HOUR_PIPS:
            self.chkPips.select()
        else:
            self.chkPips.deselect()

    def __switchOffSounds(self):
        print("switch off")
        self.lblHrChimes.configure(state="disabled")
        self.chkHrChimes.configure(state="disabled")
        self.lblQtrChimes.configure(state="disabled")
        self.chkQtrChimes.configure(state="disabled")
        self.lblPips.configure(state="disabled")
        self.chkPips.configure(state="disabled")
        self.lblVolume.configure(state="disabled")
        self.sldVolume.configure(state="disabled")

