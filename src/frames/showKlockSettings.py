###############################################################################################################
#    showKlockSettings   Copyright (C) <2024>  <Kevin Scott>                                                  #
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

import src.frames.settings.application as frmApplication
import src.frames.settings.time as frmTime
import src.frames.settings.menu as frmMenu
import src.frames.settings.font as frmFont
import src.frames.settings.sounds as frmSound

class MySettings(ctk.CTkFrame):
    """  A class that creates the frame for the settings.
    """
    def __init__(self, main, myConfig):
        super().__init__(main)

        self.main        = main
        self.myConfig    = myConfig
        self.frmSettings = {}
        self.foreColour  = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblName = ctk.CTkLabel(self, text=self.myConfig.NAME, text_color=self.foreColour,
                                    fg_color=self.myConfig.BACKGROUND)
        self.lblName.grid(row=0, column=0)
        self.lblVersion = ctk.CTkLabel(self, text=f"Version {self.myConfig.VERSION}", text_color=self.foreColour,
                                       fg_color=self.myConfig.BACKGROUND)
        self.lblVersion.grid(row=0, column=1)


        self.tvSettings =  ctk.CTkTabview(self, width=700, height=500, fg_color=self.myConfig.BACKGROUND)
        self.tvSettings.grid(row=1, column=0, columnspan=2)

        for header in self.myConfig.SETTINGS_HEADERS:
            self.frmSettings[header] = self.tvSettings.add(header)

            match header:
                case "APPLICATION":
                    frmApp = frmApplication.MyApplicationFrame(self, self.frmSettings["APPLICATION"], self.myConfig)
                    frmApp.grid(row=1, column=0)
                case "TIME":
                    frmTm = frmTime.MyTimeFrame(self, self.frmSettings["TIME"], self.myConfig)
                    frmTm.grid(row=1, column=0)
                case "MENU":
                    frmMn = frmMenu.MyMenuFrame(self, self.frmSettings["MENU"], self.myConfig)
                    frmMn.grid(row=1, column=0)
                case "FONT":
                    frmMn = frmFont.MyFontFrame(self, self.frmSettings["FONT"], self.myConfig)
                    frmMn.grid(row=1, column=0)
                case "SOUNDS":
                    frmMn = frmSound.MySoundFrame(self, self.frmSettings["SOUNDS"], self.myConfig)
                    frmMn.grid(row=1, column=0)

        self.btnExit = ctk.CTkButton(self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                     corner_radius=12, width=100, command=self.__exit)
        self.btnExit.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.btnSave = ctk.CTkButton(self, text="Save", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                     corner_radius=12, width=100, state="disabled", command=self.__Save)
        self.btnSave.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    def __exit(self):
        """  Closes the window.
        """
        self.main.destroy()

    def __Save(self):
        pass






