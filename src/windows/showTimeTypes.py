###############################################################################################################
#    showAbout.py   Copyright (C) <2024>  <Kevin Scott>                                                        #
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

class timeTypes(ctk.CTkToplevel):
    """  A class that creates a window to allow the user to change the time format.
         A list of the available time types are displayed in a drop down box.
         The size of the text can also be chosen.
    """
    def __init__(self, master, myConfig ):
        super().__init__(master)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("500x200+200+200")
        self.resizable(False, False)
        self.title("Select Time Format")

        self.selectTime = st.SelectTime()
        self.myConfig = myConfig
        self.TimeFont = ctk.CTkFont(family="default", size=20)

        self._create_widgets()

    def _create_widgets(self):
        """  Create the history display display.
        """
        timeType = self.myConfig.TIME_TYPE
        TimeSize = ["%i" % i for i in (list(range(6, 17)) + list(range(18,102, 2)))]

        lblDesc = ctk.CTkLabel(self, text="Select the format for the time display.", corner_radius=6)
        lblDesc.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")
        lblDesc = ctk.CTkLabel(self, text="Select the size for the time display.", corner_radius=6)
        lblDesc.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")
        self.cbTimeType = ctk.CTkComboBox(self, values=self.selectTime.timeTypes, command=self.changeTimeType, variable=timeType, hover=True)
        self.cbTimeType.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="ew")
        self.cbTimeSIze = ctk.CTkComboBox(self, values=TimeSize, command=self.changeTimeSize, variable=TimeSize)
        self.cbTimeSIze.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="ew")
        self.lblExample = ctk.CTkLabel(self, text=self.selectTime.getTime(timeType), font=self.TimeFont, corner_radius=6)
        self.lblExample.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="ew", columnspan=2)

        self.cbTimeType.set(self.myConfig.TIME_TYPE)
        self.cbTimeSIze.set(self.myConfig.TIME_FONT_SIZE)

    def changeTimeType(self, choice):
        """  Called when a new time type is chosen.
             The time type in the config is also changed, so the main time will change in real time.
        """
        self.myConfig.TIME_TYPE = choice
        self.lblExample.configure(text=self.selectTime.getTime(choice))
        self.cbTimeType.set(choice)

    def changeTimeSize(self, choice):
        """  Called when a new time size is chosen.
             The time size in the config is also changed, so the main time will change in real time.
        """
        self.TimeFont.configure(size=int(choice))
        self.myConfig.TIME_FONT_SIZE = int(choice)
        self.lblExample.configure(font=self.TimeFont)
        self.cbTimeSIze.set(choice)
