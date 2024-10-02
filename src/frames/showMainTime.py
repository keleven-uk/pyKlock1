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

         mt = MyStatusBarFrame()
         mt.update() - to update the main time colours.
    """
    def __init__(self, master, myConfig):
        super().__init__(master)

        self.master   = master
        self.myConfig = myConfig
        self.timeFont = ctk.CTkFont(family=self.myConfig.TIME_FONT_FAMILY, size=self.myConfig.TIME_FONT_SIZE)
        self._create_widgets()


    def _create_widgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblTime = ctk.CTkLabel(master=self, text=self._timeString(), font=self.timeFont,
                                    text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.lblTime.pack(expand=True)

        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.lblTime.bind("<B1-Motion>", self._move_window)


    def _move_window(self, event):
        """  Moves the window when the mouse is left clicked and moved.
        """
        self.master.geometry(f"+{event.x_root}+{event.y_root}")


    def _timeString(self):
        """  Returns the current time as a text string.
        """
        return time.strftime("%H:%M:%S")


    def update(self):
        """  Updates the main time text.
             The method updates both text and font.
             Method is externally called.
        """
        self.lblTime.configure(text=self._timeString())

        self.timeFont.configure(family=self.myConfig.TIME_FONT_FAMILY, size=self.myConfig.TIME_FONT_SIZE)
        self.lblTime.configure(text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND, font=self.timeFont)






