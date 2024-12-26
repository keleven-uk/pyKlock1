###############################################################################################################
#    showAbout.py   Copyright (C) <2024>  <Kevin Scott>                                                        #
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

import psutil

import platform

from PIL import Image
import datetime as dt

import customtkinter as ctk

from src.projectPaths import RESOURCE_PATH

class showAbout(ctk.CTkToplevel):
    """  A class to display general information about pyKlock.
    """
    def __init__(self, master, myConfig, myTimer):
        super().__init__(master)

        self.myConfig = myConfig
        self.myTimer  = myTimer

        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)
        ctk.set_default_color_theme(self.myConfig.COLOUR_THEME)

        self.geometry("500x640+200+200")            # width x height + xpos + ypos
        self.resizable(False, False)

        self.__createWidgets()


    def update(self):
        """  Will only be called if the window is visible.
             Updated the pyKlock up time and PC up time labels in real time.
        """
        bootTime = psutil.boot_time()
        CurrTime = dt.datetime.now().timestamp()
        elapTime = self.myTimer.formatSeconds(CurrTime-bootTime)

        self.bf.lblElapsed.configure(text=f"PC Up Time : {elapTime}")
        self.bf.lblBoot.configure(text=f"pyKlock Up Time : {self.myTimer.Elapsed}")


    def __createWidgets(self):
        """  Create the about widgets [frames].
        """
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.tf = topFrame(self, self.myConfig)
        self.tf.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.mf = middleFrame(self)
        self.mf.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.bf = bottomFrame(self)
        self.bf.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.btnExit = ctk.CTkButton(self, text="Exit", command=self.destroy)
        self.btnExit.grid(row=3, column=0, padx=(20,20), pady=(20,20))


class topFrame(ctk.CTkFrame):
    """  A class for the top form of the about window.
         The display general information about pyKlock.
    """
    def __init__(self, master, myConfig, **kwargs):
        super().__init__(master, **kwargs)

        self.border_color = "red"

        my_image = ctk.CTkImage(light_image=Image.open(f"{RESOURCE_PATH}\\tea.ico"), size=(100, 100))
        image_label = ctk.CTkLabel(self, image=my_image, text="")  # display image with a CTkLabel
        image_label.grid(row=0, column=0, padx=20, rowspan=3)
        lblAppName = ctk.CTkLabel(self, text=f"{myConfig.NAME}", font=("default", 50), justify=("center"))
        lblAppName.grid(row=0, column=1, padx=20)
        lblAppDesc = ctk.CTkLabel(self, text="A Clock with a K", font=("default", 20), justify=("center"))
        lblAppDesc.grid(row=1, column=1, padx=20)
        lblEmail = ctk.CTkLabel(self, text="klock@keleven.co.uk", font=("default", 20), justify=("center"))
        lblEmail.grid(row=2, column=1, padx=20)
        lblCopy = ctk.CTkLabel(self, text="(c) Kevin Scott 2024", font=("default", 20), justify=("center"))
        lblCopy.grid(row=3, column=1, padx=20)
        lblVersion = ctk.CTkLabel(self, text=f"pyKlock Version : {myConfig.VERSION}", font=("default", 20), justify=("center"))
        lblVersion.grid(row=4, column=1, padx=20)

class middleFrame(ctk.CTkFrame):
    """  A class for the middle form of the about window.
         The display system information.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        uname = platform.uname()

        lblTitle = ctk.CTkLabel(self,     text="System Info", font=("default", 15), justify=("left"))
        lblTitle.grid(row=0, column=0, padx=(0,0), sticky="w")
        lblNode = ctk.CTkLabel(self,     text=f"Node Name : {uname.node}", font=("default", 15), justify=("left"))
        lblNode.grid(row=1, column=0, padx=(0,0), sticky="w")
        lblSystem = ctk.CTkLabel(self,   text=f"System    : {uname.system}", font=("default", 15), justify=("left"))
        lblSystem.grid(row=2, column=0, padx=(0,0), sticky="w")
        lblRelease = ctk.CTkLabel(self,   text=f"Release  : {uname.release}", font=("default", 15), justify=("left"))
        lblRelease.grid(row=3, column=0, padx=(0,0), sticky="w")
        lblVersion = ctk.CTkLabel(self,   text=f"Version  : {uname.version}", font=("default", 15), justify=("left"))
        lblVersion.grid(row=4, column=0, padx=(0,0), sticky="w")
        lblMachine = ctk.CTkLabel(self,   text=f"Machine  : {uname.machine}", font=("default", 15), justify=("left"))
        lblMachine.grid(row=5, column=0, padx=(0,0), sticky="w")
        lblProcessor = ctk.CTkLabel(self, text=f"Processor: {uname.processor}", font=("default", 15), justify=("left"))
        lblProcessor.grid(row=6, column=0, padx=(0,0))


class bottomFrame(ctk.CTkFrame):
    """  A class for the bottom form of the about window.
         The display pyKlock and PC up time.
         The PC elapsed time is updated in the update method of the showAbout class.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.lblBoot = ctk.CTkLabel(self, text="PC Up Time : 00:00:00", font=("default", 15))
        self.lblBoot.grid(row=0, column=0, padx=(0,0), sticky="w")
        self.lblElapsed = ctk.CTkLabel(self, text="pyKlock Up Time : 00:00:00", font=("default", 15))
        self.lblElapsed.grid(row=1, column=0, padx=(0,0), sticky="w")







