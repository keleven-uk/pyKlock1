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
        self._create_widgets()


    def _create_widgets(self):
        """  Create the main time display.
        """
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=2)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.configure(fg_color=self.myConfig.BACKGROUND)

        self.lblDate = ctk.CTkLabel(master=self, text="date", text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND,
                                    anchor="w", font=self.statusFont)       #  padx - left/right.
        self.lblDate.grid(row=0, column=0, padx=(0,0), pady=(0,0), sticky="w")                                                                        #  pady - top/bottom.

        self.lblStatus = ctk.CTkLabel(master=self, text="status", text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND,
                                     font=self.statusFont)
        self.lblStatus.grid(row=0, column=1, padx=(0,20), pady=(0,0), sticky="ew")

        self.lblIdle = ctk.CTkLabel(master=self, text="idle", text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND,
                                    anchor="e", font=self.statusFont)
        self.lblIdle.grid(row=0, column=2, padx=(0,0), pady=(0,0), sticky="e")

    def update(self):
        """  Update the status bar [date - status - idle time].
             Method is externally called.

             I couldn't get the status bar to line correctly.
             I wanted the date on the left side, the status in the middle and the idle time at the far right.
             I reverted to padding the string with spaces depending on the width of the window.
             I know this is a bit klunky - will re-visit if I find a better way.
        """
        windowWidth = self.master.winfo_width()
        dateText = time.strftime("%A %d %B %Y")
        dateLeng = self.statusFont.measure(text=dateText)
        datePadd = int((windowWidth / 2) - dateLeng)
        self.lblDate.configure(text=dateText.ljust(datePadd," "), text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)

        StatusText = utils.get_state()
        StatusLeng = self.statusFont.measure(text=StatusText)
        StatusPadd = int((windowWidth / 4) - StatusLeng)
        self.lblStatus.configure(text=StatusText.center(StatusPadd), text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)

        IdleText = utils.get_idle_duration()
        IdleLeng = self.statusFont.measure(text=IdleText)
        IdlePadd = int((windowWidth / 4) - IdleLeng)
        self.lblIdle.configure(text=IdleText.rjust(IdlePadd," "), text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)

        self.configure(fg_color=self.myConfig.BACKGROUND)












