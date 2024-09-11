###############################################################################################################
#    showStatusBar   Copyright (C) <2024>  <Kevin Scott>                                                      #
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


class MyStatusBarFrame(ctk.CTkFrame):
    """  A class that creates the frame for the status bar.
    """
    def __init__(self, master):
        super().__init__(master)

        self.lblDate = ctk.CTkLabel(master=self, text="date")
        self.lblDate.grid(row=0, column=0, sticky="w")

        self.lblStatus = ctk.CTkLabel(master=self, text="status")
        self.lblStatus.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        self.lblIdle = ctk.CTkLabel(master=self, text="idle")
        self.lblIdle.grid(row=0, column=2, sticky="e")






