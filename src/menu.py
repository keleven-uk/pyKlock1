###############################################################################################################
#    menu.py   Copyright (C) <2024>  <Kevin Scott>                                                            #
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

import src.windows.SelectColourWindow as cw
import src.windows.showInfo as si

class myMenu(CTkmenu.CTkMenuBar):
    """  A class the creates the menu.

        menu = myMenu()
        menu.update() - to update the menu colours.

    """

    def __init__(self, master, myConfig, myLogger):
        super().__init__(master)

        self.master = master
        self.myConfig = myConfig
        self.myLogger = myLogger

        self._create_menu()


    def _create_menu(self):
        """  Creates the menu widgets.
        """
        self.menu = CTkmenu.CTkMenuBar(self.master)
        self.mnuFile = self.menu.add_cascade("File")
        self.mnuEdit = self.menu.add_cascade("Edit")
        self.mnuHelp = self.menu.add_cascade("Help")

        self.dropdown1 = CTkmenu.CustomDropdownMenu(widget=self.mnuFile)
        self.dropdown1.add_option(option="Exit", command=self._close)

        self.dropdown2 = CTkmenu.CustomDropdownMenu(widget=self.mnuEdit)
        self.dropdown2.add_option(option="Colour", command=self._showColourWindow)

        self.dropdown3 = CTkmenu.CustomDropdownMenu(widget=self.mnuHelp)
        self.dropdown3.add_option(option="History", command=self._showHistory)
        self.dropdown3.add_option(option="License", command=self._showLicence)
        self.dropdown3.add_separator()
        self.dropdown3.add_option(option="About")

        self.update()


    def _showLicence(self):
        """  Loads the license text file into a new window.
        """
        si.showInfo(self.master, "History")


    def _showHistory(self):
        """  Loads the history text file into a new window.
        """
        si.showInfo(self.master, "License")

    def _close(self):
        """  Called when the Exit option is chosen.  First saves the window position and colours and them closes app.
        """
        self._savePosition()
        self.master.destroy()


    def _showColourWindow(self):
        """   Calls the colour picker window.
        """
        cw.ColourWindow(self.master, self.myConfig)


    def _savePosition(self):
        """   Saves the relevant information to the config file.
        """
        self.master.update_idletasks()              #  To make sure the app location had been updated.
        appGeometry = self.master.geometry()
        appWidth    = self.master.winfo_width()
        appHeight   = self.master.winfo_height()
        appXpos     = self.master.winfo_rootx()
        appYpos     = self.master.winfo_rooty()

        self.myLogger.debug(f" Window Geom   = {appGeometry}")
        self.myLogger.debug(f" Window Width  = {appWidth}")
        self.myLogger.debug(f" Window Height = {appHeight}")
        self.myLogger.debug(f" Window X pos  = {appXpos}")
        self.myLogger.debug(f" Window Y pos  = {appYpos}")

        self.myConfig.WIN_WIDTH  = appWidth
        self.myConfig.WIN_HEIGHT = appHeight
        self.myConfig.X_POS      = appXpos
        self.myConfig.Y_POS      = appYpos

        self.myConfig.writeConfig()

    def update(self):
        """  Updates the colours of the menu from the current config.
             Method is externally called.
        """
        self.mnuFile.configure(text_color=self.myConfig.FOREGROUND)
        self.mnuEdit.configure(text_color=self.myConfig.FOREGROUND)
        self.mnuHelp.configure(text_color=self.myConfig.FOREGROUND)

        self.dropdown1.configure(text_color=self.myConfig.FOREGROUND)
        self.dropdown2.configure(text_color=self.myConfig.FOREGROUND)
        self.dropdown3.configure(text_color=self.myConfig.FOREGROUND)
