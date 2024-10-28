###############################################################################################################
#    vfdKlock   Copyright (C) <2024>  <Kevin Scott>                                                           #
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
import src.frames.showVFDTime  as vfdTime

class vfdKlock(ctk.CTkToplevel):
    """  A class to display current time using Vacuum Fluorescent Displays.
    """
    def __init__(self, master, myConfig, myLogger):
        super().__init__(master)

        self.master   = master
        self.myConfig = myConfig
        self.myLogger = myLogger

        menuWidth  = 24
        menuHeight = 2
        fontSize   = 12

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        winGeometry=f"{self.myConfig.VFD_WIDTH}x{self.myConfig.VFD_HEIGHT}+{self.myConfig.VFD_X_POS}+{self.myConfig.VFD_Y_POS}"
        self.geometry(winGeometry)

        # Using tkinter direct to remove the default title bar. transparency and always on top.
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", myConfig.VFD_BACKGROUND)
        self.attributes("-topmost", True)

        self.configure(fg_color=self.myConfig.VFD_BACKGROUND)

        self.menu    = CTkmenu.CTkMenuBar(self)
        self.mnuFile = self.menu.add_cascade("File")

        #  Exit
        self.dropdown1 = CTkmenu.CustomDropdownMenu(widget=self.mnuFile, height=menuHeight,
                                                    width=menuWidth, font=("default", fontSize))
        self.dropdown1.add_option(option="Exit", command=self._close)

        #  Create the frame for the time display.
        myLogger.info("  Creating vfdKlock Main Time")
        self.mainTime = vfdTime.showVFDime(self, myConfig)
        self.mainTime.pack(expand=True)

        #  Create the frame for the status bar.
        myLogger.info("  Creating vfdKlock Status Bar")
        self.StatusBar = myStatusBar.MyStatusBarFrame(self, self.myConfig)
        self.StatusBar.pack(expand=True)

        self.after(1000, self._update)              #  Will update the status bar.

    def _close(self):
        """  Called when the Exit option is chosen.  First saves the window position then closes app.
        """
        self.master.update_idletasks()              #  To make sure the app location had been updated.

        self.myConfig.VFD_X_POS = self.winfo_rootx()
        self.myConfig.VFD_Y_POS = self.winfo_rooty()

        self.myConfig.writeConfig()

        self.master.state("normal")
        self.master.overrideredirect(True)
        self.destroy()

    def _update(self):
        """  Updates the status bar.
        """
        self.mnuFile.configure(text_color=self.myConfig.VFD_FOREGROUND)
        self.dropdown1.configure(text_color=self.myConfig.VFD_FOREGROUND)
        self.StatusBar.update()
        self.after(30000, self._update)















