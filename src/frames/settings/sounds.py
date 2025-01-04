###############################################################################################################
#    sounds.py   Copyright (C) <2024-25>  <Kevin Scott>                                                       #
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

import src.classes.sounds as snds

class MySoundFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for the Application.

        Note : this frame uses a copy of the config file i.e. not myconfig.
    """
    def __init__(self, master, main, config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.config     = config
        self.sounds     = snds.Sounds(self.config)
        self.foreColour = "white"

        self.__createWidgets()
        self.__setWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Sound Settings", text_color="yellow", fg_color=self.config.BACKGROUND)
        self.lblTitle.grid(row=0, column=2)
        #---------------------------------------------------------------------------------------------- Sound Enabled -------------
        self.lblSound = ctk.CTkLabel(self, text="Sound Enabled", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblSound.grid(row=1, column=0, padx=10, pady=10)
        self.chkSound = ctk.CTkCheckBox(self, text="", fg_color=self.config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__setSound)
        self.chkSound.grid(row=1, column=1, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Hour Chimes ---------------
        self.lblHrChimes = ctk.CTkLabel(self, text="Hour Chimes", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblHrChimes.grid(row=2, column=0, padx=10, pady=10)
        self.chkHrChimes = ctk.CTkCheckBox(self, text="", fg_color=self.config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__hourChimes)
        self.chkHrChimes.grid(row=2, column=1, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Quarter Hour Chimes -------
        self.lblQtrChimes = ctk.CTkLabel(self, text="Quarter Hour Chimes", text_color=self.foreColour,
                                              fg_color=self.config.BACKGROUND)
        self.lblQtrChimes.grid(row=2, column=2, padx=10, pady=10)
        self.chkQtrChimes = ctk.CTkCheckBox(self, text="", fg_color=self.config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__qtrHourChimes)
        self.chkQtrChimes.grid(row=2, column=3, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- The Pips on the Hour ------
        self.lblPips = ctk.CTkLabel(self, text="The Pips on the Hour", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblPips.grid(row=3, column=0, padx=10, pady=10)
        self.chkPips = ctk.CTkCheckBox(self, text="", fg_color=self.config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__pips)
        self.chkPips.grid(row=3, column=1, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Westminster type chimes ---
        self.lblWestminster = ctk.CTkLabel(self, text="Westminster type chimes", text_color=self.foreColour,
                                              fg_color=self.config.BACKGROUND)
        self.lblWestminster.grid(row=4, column=0, padx=10, pady=10)
        self.chkWestminster = ctk.CTkCheckBox(self, text="", fg_color=self.config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__westminsterChimes)
        self.chkWestminster.grid(row=4, column=1, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Cuckoo type chimes --------
        self.lblCuckoo = ctk.CTkLabel(self, text="Cuckoo type chimes", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblCuckoo.grid(row=4, column=2, padx=10, pady=10)
        self.chkCuckoo = ctk.CTkCheckBox(self, text="", fg_color=self.config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__cuckooChimes)
        self.chkCuckoo.grid(row=4, column=3, padx=10, pady=10)

        self.lblWarning = ctk.CTkLabel(self, text="Only One type.", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblWarning.grid(row=4, column=4, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Sound Volume --------------
        self.lblVolume = ctk.CTkLabel(self, text="Sound Volume", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblVolume.grid(row=5, column=0, padx=10, pady=10)
        self.sldVolume= ctk.CTkSlider(self, from_=0, to=50, command=self.__soundVolume)
        self.sldVolume.grid(row=5, column=1, padx=10, pady=10, columnspan=2)
        self.lblCurVol = ctk.CTkLabel(self, text=f"Current Volume {self.config.SOUNDS_VOLUME}", text_color=self.foreColour,
                                              fg_color=self.config.BACKGROUND)
        self.lblCurVol.grid(row=5, column=3, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Test Volume ---------------
        self.btnTest = ctk.CTkButton( self, text="Test Volume", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self.__testVolume)
        self.btnTest.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")

    def __setSound(self):
        """  Called when sound is Enabled/disabled.
             If disabled, then tries to switch off all further sound options  [not working].
        """
        self.master.btnSave.configure(state="normal")

        if self.chkSound.get():
            self.__switchOnSounds()
            self.config.SOUNDS = True
        else:
            self.__switchOffSounds()
            self.config.SOUNDS = False

    def __hourChimes(self):
        """  Called when hourly chimes is Enabled/disabled.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkSound.get()
        self.config.SOUNDS_HOUR_CHIMES = True if clicked == 1 else False

    def __qtrHourChimes(self):
        """  Called when quarterly chimes is Enabled/disabled.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkQtrChimes.get()
        self.config.SOUNDS_QUARTER_CHIMES = True if clicked == 1 else False

    def __pips(self):
        """  Called when the pips is Enabled/disabled.

             Can only be either Westminster,Cuckoo or pips chimes.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkPips.get()
        if clicked:
            self.config.SOUNDS_HOUR_PIPS = True
            self.lblCuckoo.configure(state="disabled")
            self.chkCuckoo.configure(state="disabled")
            self.lblWestminster.configure(state="disabled")
            self.chkWestminster.configure(state="disabled")
        else:
            self.config.SOUNDS_HOUR_PIPS = False
            self.lblCuckoo.configure(state="normal")
            self.chkCuckoo.configure(state="normal")
            self.lblWestminster.configure(state="normal")
            self.chkWestminster.configure(state="normal")

        self.sounds.checkHourChimes(self)        #  There should be one and only one hour chime selected.

    def __westminsterChimes(self):
        """  Called when Westminster type chimes is Enabled/disabled.

             Can only be either Westminster,Cuckoo or pips chimes.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkWestminster.get()

        if clicked:
            self.config.SOUNDS_WESTMINSTER = True
            self.lblCuckoo.configure(state="disabled")
            self.chkCuckoo.configure(state="disabled")
            self.lblPips.configure(state="disabled")
            self.chkPips.configure(state="disabled")
        else:
            self.config.SOUNDS_WESTMINSTER = False
            self.lblCuckoo.configure(state="normal")
            self.chkCuckoo.configure(state="normal")
            self.lblPips.configure(state="normal")
            self.chkPips.configure(state="normal")

        self.sounds.checkHourChimes(self)        #  There should be one and only one hour chime selected.

    def __cuckooChimes(self):
        """  Called when Cuckoo type chimes is Enabled/disabled.

             Can only be either Westminster,Cuckoo or pips chimes.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkCuckoo.get()

        if clicked:
            self.config.SOUNDS_CUCKOO = True
            self.lblWestminster.configure(state="disabled")
            self.chkWestminster.configure(state="disabled")
            self.lblPips.configure(state="disabled")
            self.chkPips.configure(state="disabled")
        else:
            self.config.SOUNDS_WESTMINSTER = False
            self.lblWestminster.configure(state="normal")
            self.chkWestminster.configure(state="normal")
            self.lblPips.configure(state="normal")
            self.chkPips.configure(state="normal")

        self.sounds.checkHourChimes(self)        #  There should be one and only one hour chime selected.

    def __soundVolume(self, choice):
        """  Called when the sound volume is changed..
        """
        self.master.btnSave.configure(state="normal")
        volume = self.sldVolume.get()
        self.lblCurVol.configure(text=f"Current Volume {volume:0.0f}")
        self.config.SOUNDS_VOLUME = volume

    def __testVolume(self):
        """  Enable the pip to be played to test the volume.
        """
        self.sounds.playPips()

    def __setWidgets(self):
        """  Sets initial settings to sound controls.
        """
        if self.config.SOUNDS:
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
        self.sldVolume.set(self.config.SOUNDS_VOLUME)
        self.sldVolume.configure(number_of_steps=50)

        if self.config.SOUNDS_HOUR_CHIMES:
            self.chkHrChimes.select()
        else:
            self.chkHrChimes.deselect()

        if self.config.SOUNDS_QUARTER_CHIMES:
            self.chkQtrChimes.select()
        else:
            self.chkQtrChimes.deselect()

        if self.config.SOUNDS_HOUR_PIPS:
            self.chkPips.select()
        else:
            self.chkPips.deselect()

        if self.config.SOUNDS_WESTMINSTER:
            self.chkWestminster.select()
            self.lblCuckoo.configure(state="disabled")
            self.chkCuckoo.configure(state="disabled")
        else:
            self.chkWestminster.deselect()
            self.lblCuckoo.configure(state="normal")
            self.chkCuckoo.configure(state="normal")

        if self.config.SOUNDS_CUCKOO:
            self.chkCuckoo.select()
            self.lblWestminster.configure(state="disabled")
            self.chkWestminster.configure(state="disabled")
        else:
            self.chkCuckoo.deselect()
            self.lblWestminster.configure(state="normal")
            self.chkWestminster.configure(state="normal")

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
        self.lblWestminster.configure(state="disabled")
        self.chkWestminster.configure(state="disabled")
        self.lblCuckoo.configure(state="disabled")
        self.chkCuckoo.configure(state="disabled")
        self.lblVolume.configure(state="disabled")
        self.sldVolume.configure(state="disabled")

