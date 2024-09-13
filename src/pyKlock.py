###############################################################################################################
#    pyKlock   Copyright (C) <2024>  <Kevin Scott>                                                            #
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

import src.frames.showMenuButtons as myMenuButtons
import src.frames.showMainTime    as myMainTime
import src.frames.showStatusBar   as myStatusBar

class Klock(ctk.CTk):
    """  The main Klock class, when call will create the Klock main window.
         The class should be called from the main script.
    """
    def __init__(self):

        #  Call the constructor method of the parent class.
        super().__init__()

        #  Sets the appearance of the window.
        #  Supported modes : Light, Dark, System.
        #  "System" sets the appearance mode to the appearance mode of the system.
        ctk.set_appearance_mode("Dark")

        #  Sets the colour of the widgets in the window.
        #  Supported themes : green, dark-blue, blue.
        ctk.set_default_color_theme("dark-blue")

        #  Dimensions of the window
        appWidth, appHeight = (300, 160)

        self.title("Klock")
        self.geometry(f"{appWidth}x{appHeight}")
        self.configure(fg_color="black")

        # Using tkinter direct to remove the default title bar. transparency and always on top.
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", "black")
        self.attributes("-topmost", True)

        #  Create the from for the menu/buttons.
        self.menuButtons = myMenuButtons.MyMenuButtonsFrame(self)
        self.menuButtons.pack()

        #  Create the frame for the main time text.
        self.mainTime = myMainTime.MyMainTimeFrame(self)
        self.mainTime.pack(expand=True)
        self.after(1000, self.update)              #  Will update the time and status bar.

        #  Create the from for the status bar.
        self.StatusBar = myStatusBar.MyStatusBarFrame(self)
        self.StatusBar.pack()

    def update(self):
        """  Update the time and status bar.
        """
        self.mainTime.update()
        self.StatusBar.update()














