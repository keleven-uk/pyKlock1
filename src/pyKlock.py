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

import src.frames.showMainTime  as myMainTime
import src.frames.showStatusBar as myStatusBar
import src.classes.eventsStore as es
import src.classes.sounds as snds
import src.menu as myMenu


class pyKlock(ctk.CTk):
    """  The main pyKlock class, when called will create the pyKlock main window.
         The class should be called from the main script.
    """
    def __init__(self, myLogger, myConfig, myTimer):

        #  Call the constructor method of the parent class.
        super().__init__()

        self.myConfig    = myConfig
        self.myLogger    = myLogger
        self.myTimer     = myTimer                             #  Also starts the timer - used to determined pyKlock running time.
        self.sounds      = snds.Sounds(self.myConfig, self.myLogger)
        self.eventsStore = es.eventsStore(self, self.myConfig) #  This needs to be declared here and passed down the tree.
                                                               #  So the checks whether any of the events are due can be done all the time.

        #  Sets the appearance of the window.
        #  Supported modes : Light, Dark, System.
        #  "System" sets the appearance mode to the appearance mode of the system.
        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)

        #  Sets the colour of the widgets in the window.
        #  Supported themes : green, dark-blue, blue.
        ctk.set_default_color_theme(self.myConfig.COLOUR_THEME)

        #  Dimensions of the window

        self.title("pyKlock")
        self.geometry(f"{myConfig.WIN_WIDTH}x{myConfig.WIN_HEIGHT}+{myConfig.X_POS}+{myConfig.Y_POS}")
        self.resizable(False, False)
        self.configure(fg_color=myConfig.BACKGROUND)

        # Using tkinter direct to remove the default title bar. transparency and always on top.
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", myConfig.BACKGROUND)
        self.attributes("-topmost", True)

        self.sounds.checkHourChimes(self)        #  There should be one and only one hour chime selected.
        # ------------------------------------------------------------------------------------- Creating Menu ---------------------
        #  Create the main menu.
        myLogger.info("  Creating Menu")
        self.menu = myMenu.myMenu(self, self.myConfig, self.myLogger, self.myTimer, self.eventsStore)
        # ------------------------------------------------------------------------------------- Creating Main Time ----------------
        #  Create the frame for the main time text.
        myLogger.info("  Creating Main Time")
        self.mainTime = myMainTime.MyMainTimeFrame(self, self.myConfig)
        self.mainTime.pack(expand=True)

        self.after(1000, self.__update)              #  Update the time and status bar.
        self.after(1000, self.__eventUpdate)         #  Update the events every minute.
        # ------------------------------------------------------------------------------------- Creating Status Bar ---------------
        #  Create the frame for the status bar.
        myLogger.info("  Creating Status Bar")
        self.StatusBar = myStatusBar.MyStatusBarFrame(self, self.myConfig)
        self.StatusBar.pack(expand=True)

    def __update(self):
        """  Update the time and status bar.
        """
        if self.state() == "normal":                               #  Only update if pyKlock is visible.
            self.configure(fg_color=self.myConfig.BACKGROUND)
            self.menu.update()
            self.mainTime.update()
            self.StatusBar.update()                                #  Status bar.

        if self.myConfig.SOUNDS:
            self.sounds.playSounds()

        self.after(1000, self.__update)

    def __eventUpdate(self):
        """  Update the events every minute.
             This checks whether any of the events are due.
        """
        self.eventsStore.updateEvents()

        self.after(60000, self.__eventUpdate)

















