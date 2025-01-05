###############################################################################################################
#    showBinaryTime   Copyright (C) <2025>  <Kevin Scott>                                                     #
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

from PIL import Image

import src.selectTime as st
import src.projectPaths as pp
import src.utils.timeCodes as tc

class showBinaryKlock(ctk.CTkFrame):
    """  A class that creates a frame to display current time in a binary kjlock.

         showBinaryKlock as BinaryKlock
         BinaryKlock.update() - to update the time.
    """
    def __init__(self, main, master, myConfig, myLogger):
        super().__init__(main)

        self.main         = main
        self.master       = master
        self.myConfig     = myConfig
        self.myLogger     = myLogger
        self.selectTime   = st.SelectTime()
        self.klockSize    = self.myConfig.BINARYKLOCK_SIZE
        self.background   = self.myConfig.BINARYKLOCK_BACKGROUND

        self.__createWidgets()

    def __createWidgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.DIALKLOCK_BACKGROUND)

        self.img1Digit = ctk.CTkImage(dark_image=Image.open(f"{pp.RESOURCE_PATH}\\binaryKlock\\one.jpg"),
                                      size=(self.klockSize, self.klockSize))
        self.img0Digit = ctk.CTkImage(dark_image=Image.open(f"{pp.RESOURCE_PATH}\\binaryKlock\\zero.jpg"),
                                      size=(self.klockSize, self.klockSize))

        self.digits = {}
        for x in range(6):
            for y in range(4):
                self.digits[x, y] = self.image_label = ctk.CTkLabel(self, image=self.img1Digit, text="")  # display image with a CTkLabel
                self.digits[x, y].grid(row=y, column=x)

        #---------------------------------------------------------------------------------------------- Exit -----------------------
        self.lblExit = ctk.CTkLabel(self, text="X", text_color="red", fg_color=self.background, anchor="ne")
        self.lblExit.grid(row=0, column=6, padx=(0,0), pady=(0,0), sticky="ne")

        #  Bind the top right X to close.
        self.lblExit.bind("<Button-1>", self.__close)

        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.digits[0, 0].bind("<Button-1>",        self.__startMove)
        self.digits[0, 0].bind("<ButtonRelease-1>", self.__stopMove)
        self.digits[0, 0].bind("<B1-Motion>",       self.__moveWindow)

    def __close(self, event):
        self.master.update_idletasks()              #  To make sure the app location had been updated.

        self.myConfig.BINARYKLOCK_X_POS = self.winfo_rootx()
        self.myConfig.BINARYKLOCK_Y_POS = self.winfo_rooty()

        self.myConfig.writeConfig()

        self.master.state("normal")
        self.master.overrideredirect(True)
        self.main.destroy()

    #  Used to move the app.
    #  Binds start and stop to mouse left click and move to mouse move.
    def __startMove(self, event):
        self.x = event.x
        self.y = event.y
        self.configure(cursor="circle")

    def __stopMove(self, event):
        self.x = None
        self.y = None
        self.configure(cursor="arrow")

    def __moveWindow(self, event):
        """  Moves the window when the mouse is left clicked and moved.

             When the window is dragged, the mouse moves to the top left hand corner.
             Tried to cure, given up for now.

             The two above methods improve the cursor position, a lot better.
        """
        self.newX = event.x_root - self.x
        self.newY = event.y_root - self.y
        self.main.geometry(f"+{self.newX}+{self.newY}")

    def __timeString(self):
        """  Returns the current time as a text string using the Digit Time time type.
        """
        return self.selectTime.getTime("Digit Time")

    def update(self):
        """  Updates the main time text.
        """
        timeText = self.__timeString()

        for columns in range(6):
            rows = tc.binaryCodes[timeText[columns]]

            for pos, row in enumerate(rows):
                row = int(row)
                if row == 1:
                    self.digits[columns, pos].configure(image=self.img1Digit)
                else:
                    self.digits[columns, pos].configure(image=self.img0Digit)



