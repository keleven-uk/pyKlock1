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
    """
    def __init__(self, master, main, myConfig):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.myConfig   = myConfig
        self.selectTime = st.SelectTime()
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Time Settings", text_color=self.foreColour,
                                         fg_color=self.myConfig.BACKGROUND)
        self.lblTitle.grid(row=0, column=3)
        self.lblTimeType = ctk.CTkLabel(self, text="Time Type [Default]", text_color=self.foreColour,
                                              fg_color=self.myConfig.BACKGROUND)
        self.lblTimeType.grid(row=1, column=0, padx=10, pady=10)
        self.cbxTimeType = ctk.CTkComboBox(self, values=self.selectTime.timeTypes, text_color="white",
                                                 border_color="#030126", fg_color=self.myConfig.BACKGROUND,
                                                 command=self.__setTimeType)
        self.cbxTimeType.grid(row=1, column=2, padx=10, pady=10)
        self.cbxTimeType.set(self.myConfig.TIME_TYPE)

    def __setTimeType(self):
        self.master.btnSave.configure(state="normal")
