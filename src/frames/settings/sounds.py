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

        Note : this frame uses a copy of the Config file i.e. not myConfig.
    """
    def __init__(self, master, main, Config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.Config     = Config
        self.foreColour = "white"

        self.__createWidgets()
        self.__setWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.Config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Sound Settings", text_color=self.foreColour,
                                         fg_color=self.Config.BACKGROUND)
        self.lblTitle.grid(row=0, column=2)
        self.lblSound = ctk.CTkLabel(self, text="Sound Enabled", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblSound.grid(row=1, column=0, padx=10, pady=10)
        self.chkSound = ctk.CTkCheckBox(self, text="", fg_color=self.Config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__setSound)
        self.chkSound.grid(row=1, column=1, padx=10, pady=10)
        self.lblHrChimes = ctk.CTkLabel(self, text="Hour Chimes", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblHrChimes.grid(row=2, column=0, padx=10, pady=10)
        self.chkHrChimes = ctk.CTkCheckBox(self, text="", fg_color=self.Config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__hourChimes)
        self.chkHrChimes.grid(row=2, column=1, padx=10, pady=10)
        self.lblQtrChimes = ctk.CTkLabel(self, text="Quarter Hour Chimes", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblQtrChimes.grid(row=2, column=2, padx=10, pady=10)
        self.chkQtrChimes = ctk.CTkCheckBox(self, text="", fg_color=self.Config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__qtrHourChimes)
        self.chkQtrChimes.grid(row=2, column=3, padx=10, pady=10)
        self.lblPips = ctk.CTkLabel(self, text="The Pips on the Hour", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblPips.grid(row=3, column=0, padx=10, pady=10)
        self.chkPips = ctk.CTkCheckBox(self, text="", fg_color=self.Config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__pips)
        self.chkPips.grid(row=3, column=1, padx=10, pady=10)
        self.lblVolume = ctk.CTkLabel(self, text="Sound Volume", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblVolume.grid(row=4, column=0, padx=10, pady=10)
        self.sldVolume= ctk.CTkSlider(self, from_=0, to=50, command=self.__soundVolume)
        self.sldVolume.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
        self.lblCurVol = ctk.CTkLabel(self, text=f"Current Volume {self.Config.SOUNDS_VOLUME}", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblCurVol.grid(row=4, column=3, padx=10, pady=10)

    def __setSound(self):
        """  Called when sound is Enabled/disabled.
             If disabled, then tries to switch off all further sound options  [not working].
        """
        self.master.btnSave.configure(state="normal")

        if self.chkSound.get():
            print("on")
            self.__switchOnSounds()
            self.Config.SOUNDS = True
        else:
            print("off")
            self.__switchOffSounds()
            self.Config.SOUNDS = False

    def __hourChimes(self):
        """  Called when hourly chimes is Enabled/disabled.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkSound.get()
        self.Config.SOUNDS_HOUR_CHIMES = True if clicked == 1 else False

    def __qtrHourChimes(self):
        """  Called when quarterly chimes is Enabled/disabled.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkQtrChimes.get()
        self.Config.SOUNDS_QUARTER_CHIMES = True if clicked == 1 else False

    def __pips(self):
        """  Called when the pips is Enabled/disabled.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkPips.get()
        self.Config.SOUNDS_HOUR_PIPS = True if clicked == 1 else False

    def __soundVolume(self, choice):
        """  Called when the sound volume is changed..
        """
        self.master.btnSave.configure(state="normal")
        volume = self.sldVolume.get()
        self.lblCurVol.configure(text=f"Current Volume {volume:0.0f}")
        self.Config.SOUNDS_VOLUME = volume

    def __setWidgets(self):
        """  Sets initial settings to sound controls.
        """
        if self.Config.SOUNDS:
            self.chkSound.select()
            self.__switchOnSounds()
        else:
            self.chkSound.deselect()
            self.__switchOffSounds()

    def __switchOnSounds(self):
        """  Tries to switch on all sound settings.
        """
        self.chkHrChimes.configure(state="normal")
        self.chkQtrChimes.configure(state="normal")
        self.chkPips.configure(state="normal")
        self.sldVolume.configure(state="normal")
        self.sldVolume.set(self.Config.SOUNDS_VOLUME)
        self.sldVolume.configure(number_of_steps=50)

        if self.Config.SOUNDS_HOUR_CHIMES:
            self.chkHrChimes.select()
        else:
            self.chkHrChimes.deselect()

        if self.Config.SOUNDS_QUARTER_CHIMES:
            self.chkQtrChimes.select()
        else:
            self.chkQtrChimes.deselect()

        if self.Config.SOUNDS_HOUR_PIPS:
            self.chkPips.select()
        else:
            self.chkPips.deselect()

    def __switchOffSounds(self):
        """  Tries to switch off all sound settings.

             Dosn't seem to work.
        """
        self.lblHrChimes.configure(state="disabled")

        self.chkHrChimes.configure(state="disabled")
        self.lblQtrChimes.configure(state="disabled")
        self.chkQtrChimes.configure(state="disabled")
        self.lblPips.configure(state="disabled")
        self.chkPips.configure(state="disabled")
        self.lblVolume.configure(state="disabled")
        self.sldVolume.configure(state="disabled")

