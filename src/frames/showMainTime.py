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

import customtkinter as ctk

import src.selectTime as st

class MyMainTimeFrame(ctk.CTkFrame):
    """  A class that creates the frame for the main time display.

         mt = MyStatusBarFrame()
         mt.update() - to update the main time colours.
    """
    def __init__(self, main, myConfig):
        super().__init__(main)

        self.main   = main
        self.myConfig = myConfig
        self.selectTime = st.SelectTime()
        self.timeFont = ctk.CTkFont(family=self.myConfig.TIME_FONT_FAMILY, size=self.myConfig.TIME_FONT_SIZE)
        self._create_widgets()


    def _create_widgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblTime = ctk.CTkLabel(self, text=self._timeString(), font=self.timeFont,
                                    text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.lblTime.pack(expand=True)

        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.lblTime.bind("<B1-Motion>", self._move_window)


    def _move_window(self, event):
        """  Moves the window when the mouse is left clicked and moved.

             When the window is dragged, the mouse moves to the top left hand corner.
             Tried to cure, given up for now.
        """
        newX = event.x_root
        newY = event.y_root
        self.main.geometry(f"+{newX}+{newY}")


    def _timeString(self):
        """  Returns the current time as a text string using the current time type.
        """
        return self.selectTime.getTime(self.myConfig.TIME_TYPE)


    def update(self):
        """  Updates the main time text.
             The method updates both text and font.
             Method is externally called.
        """
        self.lblTime.configure(text=self._timeString())

        self.timeFont.configure(family=self.myConfig.TIME_FONT_FAMILY, size=self.myConfig.TIME_FONT_SIZE)

        newX = self.timeFont.measure(text=self._timeString())                   #  Get the length, in pixels, of the time text
        self.main.geometry(f"{newX}x{self.myConfig.WIN_HEIGHT}")                #  Dynamically sets the main window to fit.

        self.lblTime.configure(text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND, font=self.timeFont)






