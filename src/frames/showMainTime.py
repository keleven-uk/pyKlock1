###############################################################################################################
#    showMainTime   Copyright (C) <2024>  <Kevin Scott>                                                       #
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

import time

import customtkinter as ctk


class MyMainTimeFrame(ctk.CTkFrame):
    """  A class that creates the frame for the main time display.
    """
    def __init__(self, master):
        super().__init__(master)

        self.lblTime = ctk.CTkLabel(master=self, text=self.timeString(), font=('Pendule Ornamental', 100), text_color="green", fg_color="black")
        self.lblTime.pack(expand=True)


    def timeString(self):
        """  Returns the current time as a text string.
        """
        return time.strftime("%H:%M:%S")


    def update(self):
        """  Updates the main time text.
        """
        self.lblTime.configure(text=self.timeString())
        self.after(1000, self.update)

