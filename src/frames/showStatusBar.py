###############################################################################################################
#    showStatusBar   Copyright (C) <2024>  <Kevin Scott>                                                      #
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

import src.utils.klock_utils as utils


class MyStatusBarFrame(ctk.CTkFrame):
    """  A class that creates the frame for the status bar.

         sb = MyStatusBarFrame()
         sb.update() - to update the status bar colours.
    """
    def __init__(self, master, myConfig):
        super().__init__(master)
        self.master     = master
        self.myConfig   = myConfig
        self.statusFont = ctk.CTkFont(family=self.myConfig.STATUS_FONT_FAMILY, size=self.myConfig.STATUS_FONT_SIZE)
        self._createWidgets()
        self.relief="sunken"


    def _createWidgets(self):
        """  Create the main time display.
        """
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=2)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.configure(fg_color=self.myConfig.BACKGROUND)

        self.lblStatusBar = ctk.CTkLabel(master=self, text="status Bar", text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND,
                                     font=self.statusFont)
        self.lblStatusBar.pack(expand=True)


    def update(self):
        """  Update the status bar [date - status - idle time].
             Method is externally called.
        """
        factor = 0.125                                      #  To convert pixels to characters,
        windowWidth = self.master.winfo_width()             #  measure works in pixels but just works in chars.

        dateText = time.strftime("%A %d %B %Y")
        dateLeng = self.statusFont.measure(text=dateText)

        statusText = utils.get_state()
        statusLeng = self.statusFont.measure(text=statusText)

        idleText = utils.get_idle_duration()
        idleLeng = self.statusFont.measure(text=idleText)
                                                            #  Characters from now on.
        noOfSpaces = int((windowWidth - dateLeng - statusLeng - idleLeng) * factor)

        dateText   = dateText.ljust(noOfSpaces," ")
        statusText = statusText.center(noOfSpaces, " ")
        idleText   = idleText.rjust(noOfSpaces," ")

        statusBarText = f"{dateText} {statusText} {idleText}"

        # if len(statusBarText) >= (self.master.winfo_width()):
        #     print(f"oh no  statusBarText {len(statusBarText)}  windowWidth {windowWidth}  windt {self.master.winfo_width()}")

        self.lblStatusBar.configure(text=statusBarText, text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)


        self.configure(fg_color=self.myConfig.BACKGROUND)












