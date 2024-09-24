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
        self.myConfig = myConfig
        self._create_widgets()


    def _create_widgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)

        self.lblDate = ctk.CTkLabel(master=self, text="date", text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)       #  padx - left/right.
        self.lblDate.grid(row=0, column=0, padx=(0,0), pady=(0,0), sticky="sw")                                                             #  pady - top/bottom.

        self.lblStatus = ctk.CTkLabel(master=self, text="status", text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.lblStatus.grid(row=0, column=1, padx=(20,20), pady=(0,0), sticky="sew")

        self.lblIdle = ctk.CTkLabel(master=self, text="idle", text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.lblIdle.grid(row=0, column=2, padx=(0,0), pady=(0,0), sticky="se")

    def update(self):
        """  Update the status bar [date - status - idle time].
             Method is externally called.
        """
        self.lblDate.configure(text=time.strftime("%A %d %B %Y"))
        self.lblStatus.configure(text=utils.get_state())
        self.lblIdle.configure(text=utils.get_idle_duration())
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblDate.configure(text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.lblStatus.configure(text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.lblIdle.configure(text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)











