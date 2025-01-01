###############################################################################################################
#    showDialTime   Copyright (C) <2025>  <Kevin Scott>                                                       #
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

from tkdial import Meter

import src.selectTime as st


class showDialKlock(ctk.CTkFrame):
    """  A class that creates a frame to display current time using Speedometer type dials.

         showDialTime as dialTime
         dialTime.update() - to update the time.
    """
    def __init__(self, main, master, myConfig, myLogger):
        super().__init__(main)

        self.main         = main
        self.master       = master
        self.myConfig     = myConfig
        self.myLogger     = myLogger
        self.selectTime   = st.SelectTime()
        self.klockSize    = self.myConfig.DIALKLOCK_SIZE
        self.background   = self.myConfig.DIALKLOCK_BACKGROUND
        self.textColour   = self.myConfig.DIALKLOCK_TEXT_COLOUR
        self.scaleColour  = self.myConfig.DIALKLOCK_SCALE_COLOUR
        self.needleColour = self.myConfig.DIALKLOCK_NEEDLE_COLOUR
        self.startAngle   = 230
        self.endAngle     = -280

        self.__createWidgets()

    def __createWidgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.DIALKLOCK_BACKGROUND)
        #---------------------------------------------------------------------------------------------- Hours ----------------------
        #  state - Unbind/Bind the mouse movement with the needle.  Seems to be set to "normal" to bind.
        self.mtrHour = Meter(self, radius=self.klockSize, start=0, end=24, border_width=0,
                    fg=self.background, start_angle=self.startAngle, end_angle=self.endAngle,
                    text_font="DS-Digital 30", scale_color=self.scaleColour, needle_color=self.needleColour,
                    major_divisions=1, text_color=self.textColour, bg=self.background, state="Unbind")
        self.mtrHour.set_mark(20, 24) # set red marking from 140 to 160
        self.mtrHour.grid(row=0, column=0, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Minutes --------------------
        self.mtrMinutes = Meter(self, radius=self.klockSize, start=0, end=60, border_width=0,
                    fg=self.background, start_angle=self.startAngle, end_angle=self.endAngle,
                    text_font="DS-Digital 30", scale_color=self.scaleColour, needle_color=self.needleColour,
                    major_divisions=5, text_color=self.textColour, bg=self.background)
        self.mtrMinutes.set_mark(50, 60) # set red marking from 140 to 160
        self.mtrMinutes.grid(row=0, column=1, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Seconds --------------------
        self.mtrSeconds = Meter(self, radius=self.klockSize, start=0, end=60, border_width=0,
                    fg=self.background, start_angle=self.startAngle, end_angle=self.endAngle,
                    text_font="DS-Digital 30", scale_color=self.scaleColour, needle_color=self.needleColour,
                    major_divisions=5, text_color=self.textColour, bg=self.background)
        self.mtrSeconds.set_mark(50, 60) # set red marking from 140 to 160
        self.mtrSeconds.grid(row=0, column=2, padx=10, pady=10)
        #---------------------------------------------------------------------------------------------- Exit -----------------------
        self.lblExit = ctk.CTkLabel(self, text="X", text_color="red", fg_color=self.background, anchor="ne")
        self.lblExit.grid(row=0, column=4, padx=(0,0), pady=(0,0), sticky="ne")


        #  Bind the top right X to close.
        self.lblExit.bind("<Button-1>", self.__close)

        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.mtrHour.bind("<Button-1>",        self.__startMove)
        self.mtrHour.bind("<ButtonRelease-1>", self.__stopMove)
        self.mtrHour.bind("<B1-Motion>",       self.__moveWindow)

    def __close(self, event):
        self.master.update_idletasks()              #  To make sure the app location had been updated.

        self.myConfig.DIALKLOCK_X_POS = self.winfo_rootx()
        self.myConfig.DIALKLOCK_Y_POS = self.winfo_rooty()

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

    def update(self):
        """  Updates the main time text.
        """
        hours, minutes, seconds = self.selectTime.getNowTime()
        self.mtrHour.set(hours)      # set value
        self.mtrMinutes.set(minutes) # set value
        self.mtrSeconds.set(seconds) # set value






