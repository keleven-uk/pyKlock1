###############################################################################################################
#    showMenuButtons   Copyright (C) <2024>  <Kevin Scott>                                                    #
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


class MyMenuButtonsFrame(ctk.CTkFrame):
    """  A class that creates the frame for the menu / buttons.
    """
    def __init__(self, master):
        super().__init__(master)

        self.se = ctk.CTkSegmentedButton(self, values=["Type", "Colour", "Font"], command=self.callback, unselected_color="white", text_color="Black")
        self.se.grid(row=0, column=1, padx=20, pady=20, sticky="ew")


    # Callback function to handle segmented button clicks
    def callback(self, value):
        pass



