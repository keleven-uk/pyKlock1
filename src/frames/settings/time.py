###############################################################################################################
#    time.py   Copyright (C) <2024>  <Kevin Scott>                                                            #
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

import src.selectTime as st

class MyTimeFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for the Application.

         Note : this frame uses a copy of the Config file i.e. not myConfig.
    """
    def __init__(self, master, main, Config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.Config     = Config
        self.selectTime = st.SelectTime()
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the Time settings frame.
        """
        self.configure(fg_color=self.Config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Time Settings", text_color=self.foreColour,
                                         fg_color=self.Config.BACKGROUND)
        self.lblTitle.grid(row=0, column=3)
        self.lblTimeType = ctk.CTkLabel(self, text="Time Type [Default]", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblTimeType.grid(row=1, column=0, padx=10, pady=10)
        self.cbxTimeType = ctk.CTkComboBox(self, values=self.selectTime.timeTypes, text_color="white",
                                                 border_color="#030126", fg_color=self.Config.BACKGROUND,
                                                 command=self.__setTimeType)
        self.cbxTimeType.grid(row=1, column=1, padx=10, pady=10)
        self.cbxTimeType.set(self.Config.TIME_TYPE)
        self.lblCapitalise = ctk.CTkLabel(self, text="Capitalise main time text", text_color=self.foreColour,
                                              fg_color=self.Config.BACKGROUND)
        self.lblCapitalise.grid(row=1, column=2, padx=10, pady=10)
        self.chkCapitalise = ctk.CTkCheckBox(self, text="", fg_color=self.Config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__setCapitalise)
        self.chkCapitalise.grid(row=1, column=3, padx=10, pady=10)

        if self.Config.TIME_CAPITALISE:
            self.chkCapitalise.select()
        else:
            self.chkCapitalise.deselect()

    def __setTimeType(self, choice):
        """  A new time type has been selected.
             Enable the save button in the parent window and amend the config file with then new time type.
        """
        self.master.btnSave.configure(state="normal")
        self.Config.TIME_TYPE = choice

    def __setCapitalise(self):
        """
        """
        self.master.btnSave.configure(state="normal")
        capitalise = self.chkCapitalise.get()
        self.Config.TIME_CAPITALISE = True if capitalise == 1 else False
