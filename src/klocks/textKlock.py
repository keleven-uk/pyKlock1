###############################################################################################################
#    textKlock   Copyright (C) <2024>  <Kevin Scott>                                                          #
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

import CTkMenuBar as CTkmenu

import src.frames.showStatusBar as myStatusBar
import src.frames.showTextTime  as textTime

class textKlock(ctk.CTkToplevel):
    """  A class to display current time in text.
    """
    def __init__(self, master, myConfig, myLogger):
        super().__init__(master)

        self.master   = master
        self.myConfig = myConfig
        self.myLogger = myLogger

        menuWidth  = 24
        menuHeight = 2
        fontSize   = 12

        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)
        ctk.set_default_color_theme(self.myConfig.COLOR_THEME)

        winGeometry=f"{self.myConfig.TEXT_WIDTH}x{self.myConfig.TEXT_HEIGHT}+{self.myConfig.TEXT_X_POS}+{self.myConfig.TEXT_Y_POS}"
        self.geometry(winGeometry)

        # Using tkinter direct to remove the default title bar. transparency and always on top.
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", myConfig.TEXT_BACKGROUND)
        self.attributes("-topmost", True)

        self.configure(fg_color=self.myConfig.TEXT_BACKGROUND)

        #  Create the frame for the time display.
        myLogger.info("  Creating textKlock Main Time")
        self.mainTime = textTime.showTextime(self, self.master, self.myConfig, self.myLogger)
        self.mainTime.pack(expand=True)

        #  Create the frame for the status bar.
        myLogger.info("  Creating textKlock Status Bar")
        self.StatusBar = myStatusBar.MyStatusBarFrame(self, self.myConfig)
        self.StatusBar.pack(expand=True)

        self.after(1000, self._update)              #  Will update the status bar.

    def _update(self):
        """  Updates the status bar.
        """
        self.StatusBar.update()
        self.after(1000, self._update)















