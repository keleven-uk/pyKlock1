###############################################################################################################
#    menu.py   Copyright (C) <2024-25>  <Kevin Scott>                                                         #
#    For changes see history.txt                                                                              #
#                                                                                                             #
#    Menu used is from https://github.com/Akascape/CTkMenuBar.                                                #
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

import CTkMenuBar as CTkmenu

from tkfontchooser import askfont

import src.windows.showInfo as si
import src.windows.showHelp as sh
import src.windows.showEvents as se
import src.windows.showFriends as sf
import src.windows.showSettings as ss
import src.windows.showAbout as about
import src.windows.showTimeTypes as stt
import src.windows.SelectColourWindow as cw

import src.klocks.vfdKlock as vfdKlock
import src.klocks.textKlock as textKlock
import src.klocks.dialKlock as dialKlock

class myMenu(CTkmenu.CTkMenuBar):
    """  A class the creates the menu.

        menu = myMenu()
        menu.update() - to update the menu colours.

    """

    def __init__(self, master, myConfig, myLogger, myTimer, eventsStore):
        super().__init__(master)

        self.master        = master
        self.myConfig      = myConfig
        self.myLogger      = myLogger
        self.myTimer       = myTimer
        self.eventsStore   = eventsStore
        self.aboutTopLevel = None

        self.__createMenu()


    def __createMenu(self):
        """  Creates the menu widgets.
        """
        menuWidth  = 20
        menuHeight = 2
        fontSize   = 12

        self.menu      = CTkmenu.CTkMenuBar(self.master)
        self.mnuFile   = self.menu.add_cascade("File")
        self.mnupyKlocks = self.menu.add_cascade("Klocks")
        self.mnuThings = self.menu.add_cascade("Things")
        self.mnuEdit   = self.menu.add_cascade("Edit")
        self.mnuHelp   = self.menu.add_cascade("Help")

        #  File
        self.dropdown1 = CTkmenu.CustomDropdownMenu(widget=self.mnuFile, height=menuHeight,
                                                    width=menuWidth, font=("default", fontSize))
        self.dropdown1.add_option(option="Settings", command=self.__showSettings)
        self.dropdown1.add_separator()
        self.dropdown1.add_option(option="Exit", command=self.__close)

        #pyKlocks
        self.dropdown2 = CTkmenu.CustomDropdownMenu(widget=self.mnupyKlocks, height=menuHeight,
                                                    width=menuWidth, font=("default", fontSize))
        self.dropdown2.add_option(option="vfdKlock",  command=self.__showVFDKlock)
        self.dropdown2.add_option(option="textKlock", command=self.__showTextKlock)
        self.dropdown2.add_option(option="dialKlock", command=self.__showDialKlock)

        #  Things
        self.dropdown3  = CTkmenu.CustomDropdownMenu(widget=self.mnuThings, height=menuHeight,
                                                    width=menuWidth, font=("default", fontSize))
        self.dropdown3.add_option(option="Friends", command=self.__showFriends)
        self.dropdown3.add_option(option="Events",  command=self.__showEvents)

        #  Edit
        self.dropdown4 = CTkmenu.CustomDropdownMenu(widget=self.mnuEdit, height=menuHeight,
                                                    width=menuWidth, font=("default", fontSize))
        self.dropdown4.add_option(option="Font", command=self.__showFont)
        self.dropdown4.add_option(option="Time Type", command=self.__showTimeType)
        self.dropdown4.add_option(option="Colour", command=self.__showColourWindow)

        #  Help
        self.dropdown5 = CTkmenu.CustomDropdownMenu(widget=self.mnuHelp, height=menuHeight,
                                                    width=menuWidth, font=("default", fontSize))
        self.dropdown5.add_option(option="Help", command=self.__showHelp)
        self.dropdown5.add_separator()
        self.dropdown5.add_option(option="History", command=self.__showHistory)
        self.dropdown5.add_option(option="License", command=self.__showLicence)
        self.dropdown5.add_separator()
        self.dropdown5.add_option(option="About", command=self.__showAbout)

        self.update()


    def __showSettings(self):
        ss.showSettings(self.master, self.myConfig, self.myLogger)

    def __showDialKlock(self):
        self.master.overrideredirect(False)
        self.master.state("iconic")
        dialKlock.dialKlock(self.master, self.myConfig, self.myLogger)

    def __showTextKlock(self):
        self.master.overrideredirect(False)
        self.master.state("iconic")
        textKlock.textKlock(self.master, self.myConfig, self.myLogger)

    def __showVFDKlock(self):
        self.master.overrideredirect(False)
        self.master.state("iconic")
        vfdKlock.vfdKlock(self.master, self.myConfig, self.myLogger)

    def __showFriends(self):
        """  Loads the Friends window.
        """
        sf.FriendsWindow(self.master, self.myConfig)

    def __showEvents(self):
        """  Loads the Events window.
        """
        se.EventsWindow(self.master, self.myConfig, self.eventsStore)

    def __showHelp(self):
        """  Loads the Help file.
        """
        sh.showHelp(self.master, self.myConfig)

    def __showAbout(self):
        """  Loads the license text file into a new window.
        """
        self.aboutTopLevel = about.showAbout(self.master, self.myConfig, self.myTimer)

    def __showLicence(self):
        """  Loads the license text file into a new window.
        """
        si.showInfo(self.master, "License", self.myLogger, self.myConfig)

    def __showHistory(self):
        """  Loads the history text file into a new window.
        """
        si.showInfo(self.master, "History", self.myLogger, self.myConfig)

    def __close(self):
        """  Called when the Exit option is chosen.  First saves the window position and colours and them closes app.
        """
        self.__savePosition()
        self.master.destroy()

    def __showFont(self):
        """  Open the font chooser and get the font selected by the user.
             The font name and size are then save to myConfig for later use.
        """
        font = askfont(self)
        # font is "" if the user has cancelled
        if font:
            # spaces in the family name need to be escaped
            #font['family'] = font['family'].replace(' ', '\\ ')
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
            if font["underline"]:
                font_str += " underline"
            if font["overstrike"]:
                font_str += " overstrike"

            self.myConfig.TIME_FONT_FAMILY = font["family"]
            self.myConfig.TIME_FONT_SIZE   = font["size"]

    def __showTimeType(self):
        """   Opens a windows which allows the choice of time type display format and size..
        """
        stt.timeTypes(self, self.myConfig)

    def __showColourWindow(self):
        """   Calls the colour picker window.
        """
        cw.ColourWindow(self.master, self.myConfig)

    def __savePosition(self):
        """   Saves the relevant information to the config file.
        """
        self.master.update_idletasks()              #  To make sure the app location had been updated.
        appWidth    = self.master.winfo_width()
        appHeight   = self.master.winfo_height()
        appXpos     = self.master.winfo_rootx()
        appYpos     = self.master.winfo_rooty()

        self.myLogger.debug(f" Window Width  = {appWidth}")
        self.myLogger.debug(f" Window Height = {appHeight}")
        self.myLogger.debug(f" Window X pos  = {appXpos}")
        self.myLogger.debug(f" Window Y pos  = {appYpos}")

        #self.myConfig.WIN_WIDTH  = appWidth                    #  The width may change to fit the time test, do we need to save it.
        #self.myConfig.WIN_HEIGHT = appHeight
        self.myConfig.X_POS      = appXpos
        self.myConfig.Y_POS      = appYpos

        self.myConfig.writeConfig()

    def update(self):
        """  Updates the colours of the menu from the current config.
             Method is externally called.
        """
        self.mnuFile.configure(text_color=self.myConfig.FOREGROUND)
        self.mnuThings.configure(text_color=self.myConfig.FOREGROUND)
        self.mnuEdit.configure(text_color=self.myConfig.FOREGROUND)
        self.mnuHelp.configure(text_color=self.myConfig.FOREGROUND)
        self.mnupyKlocks.configure(text_color=self.myConfig.FOREGROUND)

        self.dropdown1.configure(text_color=self.myConfig.FOREGROUND)
        self.dropdown2.configure(text_color=self.myConfig.FOREGROUND)
        self.dropdown3.configure(text_color=self.myConfig.FOREGROUND)
        self.dropdown4.configure(text_color=self.myConfig.FOREGROUND)
        self.dropdown4.configure(text_color=self.myConfig.FOREGROUND)

        #  Only update the about window if it exists.
        if self.aboutTopLevel is None or not self.aboutTopLevel.winfo_exists():
            self.aboutTopLevel = None
        else:
            self.aboutTopLevel.update()

