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

import src.windows.SelectColourWindow as cw


class MyMenuButtonsFrame(ctk.CTkFrame):
    """  A class that creates the frame for the menu / buttons.
    """
    def __init__(self, master, myConfig, myLogger):
        super().__init__(master)

        self.master   = master
        self.myConfig = myConfig
        self.myLogger = myLogger
        self.create_widgets()


    def create_widgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.sbMenu = ctk.CTkSegmentedButton(self, values=["Type", "Colour", "Font", "Exit"],
                                             command=self.callback, unselected_color=self.myConfig.BACKGROUND,
                                             text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.sbMenu .grid(row=0, column=1, padx=(20, 20), sticky="new")


    # Callback function to handle segmented button clicks.
    def callback(self, value):
        """  Called when the Exit button is pressed.
             Saves the window position before calling destroy.
                The windows position is obtained using tkinter direct.

             The app's size if fixed at 300x150 at the moment, but might not be in the future - so we save for the future.
        """
        match value:
            case "Exit":
                self.savePosition()
                self.master.destroy()
            case "Colour":
                self.showColourWindow()
                self.sbMenu.configure(unselected_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)


    def showColourWindow(self):
        cw.ColourWindow(self.master, self.myConfig)


    def savePosition(self):
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
        """  Update the Menu Buttons].
        """
        self.sbMenu.configure(unselected_color=self.myConfig.BACKGROUND, text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)


