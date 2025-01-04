###############################################################################################################
#    menu.py   Copyright (C) <2024-25>  <Kevin Scott>                                                         #
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

class MyMenuFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for the Application.

        Note : this frame uses a copy of the config file i.e. not myconfig.
    """
    def __init__(self, master, main, config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.config     = config
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.config.BACKGROUND)
        self.lblTitle = ctk.CTkLabel(self, text="Menu Settings", text_color="yellow", fg_color=self.config.BACKGROUND)
        self.lblTitle.grid(row=0, column=3)
        #---------------------------------------------------------------------------------------------- Menu Visable ---------------
        self.lblMenuVisable = ctk.CTkLabel(self, text="Menu Visable", text_color=self.foreColour, fg_color=self.config.BACKGROUND)
        self.lblMenuVisable.grid(row=1, column=0, padx=10, pady=10)
        self.chkMenuVisable = ctk.CTkCheckBox(self, text="", fg_color=self.config.BACKGROUND, border_color=self.foreColour,
                                              hover_color="gray", command=self.__setMenuVisable)
        self.chkMenuVisable.grid(row=1, column=1, padx=10, pady=10)
        if self.config.MENU_VISIBLE:
            self.chkMenuVisable.select()
        else:
            self.chkMenuVisable.deselect()
        self.lblLabel = ctk.CTkLabel(self, text=" Setting not yet implemented", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblLabel.grid(row=1, column=3)


    def __setMenuVisable(self):
        """  Set if the menu's are visible.
             This feature is not yet implemented and may be removed.
        """
        self.master.btnSave.configure(state="normal")
        clicked = self.chkMenuVisable.get()
        self.config.MENU_VISIBLE = True if clicked == 1 else False

