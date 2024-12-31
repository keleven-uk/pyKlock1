###############################################################################################################
#    showpyKlockSettings   Copyright (C) <2024>  <Kevin Scott>                                                  #
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

from CTkMessagebox import CTkMessagebox

import src.config as Config
import src.projectPaths as pp
import src.frames.settings.application as frmApplication
import src.frames.settings.time as frmTime
import src.frames.settings.menu as frmMenu
import src.frames.settings.font as frmFont
import src.frames.settings.klocks as frmpyKlocks
import src.frames.settings.sounds as frmSound
import src.frames.settings.events as frmEvents

class MySettings(ctk.CTkFrame):
    """  A class that creates the frame for the settings.
    """
    def __init__(self, main, myConfig, myLogger):
        super().__init__(main)

        self.main        = main
        self.myConfig    = myConfig
        self.myLogger    = myLogger
        self.frmSettings = {}
        self.foreColour  = "white"
        self.copyConfig  = Config.Config(pp.CONFIG_PATH, pp.VERSION_PATH, self.myLogger)         # Create the copy config.

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


        self.tvSettings =  ctk.CTkTabview(self, width=700, height=420, fg_color=self.myConfig.BACKGROUND)
        self.tvSettings.grid(row=1, column=0, columnspan=2)

        for header in self.myConfig.SETTINGS_HEADERS:
            self.frmSettings[header] = self.tvSettings.add(header)

            match header:
                case "APPLICATION":
                    frmApp = frmApplication.MyApplicationFrame(self, self.frmSettings["APPLICATION"], self.copyConfig)
                    frmApp.grid(row=1, column=0)
                case "TIME":
                    frmTm = frmTime.MyTimeFrame(self, self.frmSettings["TIME"], self.copyConfig)
                    frmTm.grid(row=1, column=0)
                case "MENU":
                    frmMn = frmMenu.MyMenuFrame(self, self.frmSettings["MENU"], self.copyConfig)
                    frmMn.grid(row=1, column=0)
                case "FONT":
                    frmMn = frmFont.MyFontFrame(self, self.frmSettings["FONT"], self.copyConfig)
                    frmMn.grid(row=1, column=0)
                case "KLOCKS":
                    frmKl = frmpyKlocks.MypyKlocksFrame(self, self.frmSettings["KLOCKS"], self.copyConfig)
                    frmKl.grid(row=1, column=0)
                case "SOUNDS":
                    frmMn = frmSound.MySoundFrame(self, self.frmSettings["SOUNDS"], self.copyConfig)
                    frmMn.grid(row=1, column=0)
                case "EVENTS":
                    frmMn = frmEvents.MyEventsFrame(self, self.frmSettings["EVENTS"], self.copyConfig)
                    frmMn.grid(row=1, column=0)

        self.btnExit = ctk.CTkButton(self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                     corner_radius=12, width=100, command=self.__exit)
        self.btnExit.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.btnSave = ctk.CTkButton(self, text="Save", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                     corner_radius=12, width=100, state="disabled", command=self.__Save)
        self.btnSave.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    def __exit(self):
        """  Closes the window.
             Will display a warning if any settings have been changed and not saved.
        """
        try:
            if self.myConfig != self.copyConfig:
                msg = CTkMessagebox(title="Unsaved data", message="Do you really want exit, there is unsaved data?",
                                    icon="question", option_1="Yes", option_2="No")
                if msg.get()=="No":
                    return
        except NotImplemented as error:
            self.myLogger.error(f"  Problems with comparing configs for equality :: {error}")

        self.myLogger.debug("  Exited setting window although there was unsaved data.")
        self.main.destroy()

    def __Save(self):
        """  Save amended config file.
             We first copy the amended configs [copyConfig] back to the main config [myConfig].
                This ensure the amendments will be used by the rest of pyKlock.
        """
        self.myConfig.copy(self.copyConfig)
        self.myConfig.writeConfig()
        self.btnSave.configure(state="disabled")








