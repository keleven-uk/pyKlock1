###############################################################################################################
#    showNotification.py   Copyright (C) <2024>  <Kevin Scott>                                                #
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

class notification(ctk.CTkToplevel):
    """  A class to display a notification - i.e. a windows toast.
         The notifications will be displayed on the right hand side of the screen and stack from the bottom.
         The notification should fade in and fade out.

         The notification uses a class variable to keep track of how many notifications there are.

         use:
                notification = notification(self, "red")    #  Colour of the background.
                answer = notification.get()          # get answer - either Acknowledge or Mute.

         TODO:
                Need to track when a notification is dismissed and mark that screen slot as free.
    """
    noToast = -1                                    #  Class variable, to track notification numbers.

    def __init__(self, master, message, stageColour):
        super().__init__(master)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        notification.noToast += 1

        self.screenWidth  = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.noToast      = notification.noToast         #  make a local copy of the class variable.
        self.master       = master
        self.stageColour  = stageColour
        self.message      = message
        self.maxAlpha     = 0.75
        self.fadeSpeed    = 11
        self.event        =  ""

        self.width  = 300
        self.height = 100
        self.x_pos  = self.screenWidth  - self.width
        self.y_pos  = self.screenHeight - self.height - (self.noToast*self.height)

        self.geometry(f"{self.width}x{self.height}+{self.x_pos}+{self.y_pos}")
        self.resizable(True, False)

        # Using tkinter direct to remove the default title bar. transparency and always on top.
        self.configure(fg_color=self.stageColour)
        self.overrideredirect(True)
        self.attributes("-alpha", 0)
        self.attributes("-topmost", True)

        self._createWidgets()
        self._fadeIn()

    def _createWidgets(self):
        """  Create the main event display.
        """
        self.lblMessage = ctk.CTkLabel(self, text=self.message, text_color="black", fg_color="transparent")
        self.lblMessage.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
        self.btnAcknowledge = ctk.CTkButton(self, text="Acknowledge", text_color="black", fg_color="transparent", font=("Montserrat", 16),
                                    hover=False, corner_radius=12, width=100, command=self._Acknowledge)
        self.btnAcknowledge.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.btnMute = ctk.CTkButton(self, text="Mute", text_color="black", fg_color="transparent", font=("Montserrat", 16),
                                     hover=False, corner_radius=12, width=100, command=self._mute)
        self.btnMute.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

    def _fadeIn(self):
        """  Fades in the windows, but slowly increasing the alpha attribute of the background colour.

            See https://stackoverflow.com/questions/22491488/how-to-create-a-fade-out-effect-in-tkinter-my-code-crashes
        """
        alpha = self.attributes("-alpha")
        alpha = min(alpha + .01, self.maxAlpha)
        self.attributes("-alpha", alpha)
        if alpha < self.maxAlpha:
            self.after(self.fadeSpeed, self._fadeIn)

    def _fadeOut(self):
        """  Fades out the windows, but slowly decreasing the alpha attribute of the background colour.

            See https://stackoverflow.com/questions/22491488/how-to-create-a-fade-out-effect-in-tkinter-my-code-crashes
        """
        alpha = self.attributes("-alpha")
        if alpha > 0:
            alpha -= .01
            self.attributes("-alpha", alpha)
            self.after(self.fadeSpeed, self._fadeOut)
        else:
            self.destroy()

    def _Acknowledge(self):
        """  Returns a acknowledge string when the Acknowledge button is pressed.
        """
        self._fadeOut()
        self.event  =  "Acknowledge"

    def _mute(self):
        """  Returns a mute string when the Mute button is pressed.
        """
        self._fadeOut()
        self.event  =  "mute"

    def get(self):
        """  Return the appropriate return string when requested.
             Will wait until the window is destroyed before returning - calling program will wait.
        """
        if self.winfo_exists():
            self.master.wait_window(self)
        self.master.update_idletasks()              #  To make sure the app been updated.
        return self.event



