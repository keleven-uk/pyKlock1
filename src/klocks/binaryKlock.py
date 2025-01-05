###############################################################################################################
#    binaryKlock   Copyright (C) <2025>  <Kevin Scott>                                                        #
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

import src.frames.showStatusBar as myStatusBar
import src.frames.showBinaryTime as BinaryKlock

class binaryKlock(ctk.CTkToplevel):
    """  A class to display current time using a binary Klock.
    """
    def __init__(self, master, myConfig, myLogger):
        super().__init__(master)

        self.master     = master
        self.myConfig   = myConfig
        self.myLogger   = myLogger
        self.klockSize  = self.myConfig.BINARYKLOCK_SIZE
        self.background = self.myConfig.BINARYKLOCK_BACKGROUND
        self.winWidth   = (self.klockSize * 6) + 30
        self.winHeight  = (self.klockSize * 4) + 30

        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)
        ctk.set_default_color_theme(self.myConfig.COLOUR_THEME)

        winGeometry=f"{self.winWidth}x{self.winHeight}+{self.myConfig.BINARYKLOCK_X_POS}+{myConfig.BINARYKLOCK_Y_POS}"
        self.geometry(winGeometry)

        # Using tkinter direct to remove the default title bar. transparency and always on top.
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", self.background)
        self.attributes("-topmost", True)
        self.configure(fg_color=self.background)

        self.configure(fg_color=self.background)

        #  Create the frame for the time display.
        self.mainTime = BinaryKlock.showBinaryKlock(self, self.master, self.myConfig, self.myLogger)
        self.mainTime.pack(expand=True)

        #  Create the frame for the status bar.
        self.StatusBar = myStatusBar.MyStatusBarFrame(self, self.myConfig)
        self.StatusBar.pack(expand=True)

        self.after(1000, self.__update)              #  Will update the status bar.

    def __update(self):
        """  Updates the status bar and the time frame.
        """
        self.StatusBar.update()
        self.mainTime.update()
        self.after(1000, self.__update)















