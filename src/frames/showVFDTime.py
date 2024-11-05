###############################################################################################################
#    showVFDTime   Copyright (C) <2024>  <Kevin Scott>                                                        #
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

import tkVFD

import src.selectTime as st


class showVFDime(ctk.CTkFrame):
    """  A class that creates the frame for the main time display.

         vfd = showVFDime()
         cfd.update() - to update the time and status bar.
    """
    def __init__(self, main, myConfig, myLogger):
        super().__init__(main)

        myLogger.debug("  Start of showVFDime __init__")
        self.main       = main
        self.myConfig   = myConfig
        self.myLogger   = myLogger
        self.selectTime = st.SelectTime()
        self.configure(fg_color=self.myConfig.VFD_BACKGROUND)
        self._createWidgets()
        self.after(1000, self._update)              #  Will update the time.
        myLogger.debug("  End of showVFDime __init__")

    def _createWidgets(self):
        """  Create the main time display.
        """
        self.myLogger.debug("  Start of showVFDime _createWidgets")
        vfdHeight  = 200

        #  Oncolour expects a RGB row vector, bgcolour will take a normal TK colour code though.
        onColour = [int(self.myConfig.VFD_FOREGROUND[1:3], 16), int(self.myConfig.VFD_FOREGROUND[3:5], 16),
                    int(self.myConfig.VFD_FOREGROUND[5:7], 16)]
        bgColour = self.myConfig.VFD_BACKGROUND

        self.myLogger.debug("  Start of showVFDime create hour segments")
        self.hour0 = tkVFD.seg7(self, height=vfdHeight, use_CC=False, on_color=onColour, bg=bgColour)
        self.hour0.grid(row=0, column=0, padx=(0,0), pady=(0,0))
        self.hour0.char("8", DP=None, CC=0)
        self.hour1 = tkVFD.seg7(self, height=vfdHeight, use_CC=True, on_color=onColour, bg=bgColour)
        self.hour1.grid(row=0, column=1, padx=(0,0), pady=(0,0))
        self.hour1.char("8", DP=None, CC=0)

        self.myLogger.debug("  Start of showVFDime create mins segments")
        self.mins0 = tkVFD.seg7(self, height=vfdHeight, use_CC=False, on_color=onColour, bg=bgColour)
        self.mins0.grid(row=0, column=2, padx=(0,0), pady=(0,0))
        self.mins0.char("8", DP=None, CC=0)
        self.mins1 = tkVFD.seg7(self, height=vfdHeight, use_CC=False, on_color=onColour, bg=bgColour)
        self.mins1.grid(row=0, column=3, padx=(0,0), pady=(0,0))
        self.mins1.char("8", DP=None, CC=0)
        #
        # self.secs0 = tkVFD.seg7(self, height=vfdHeight, use_CC=True, on_color=onColour, bg=bgColour)
        # self.secs0.grid(row=0, column=4, padx=(0,0), pady=(0,0))
        # self.secs0.char("8", DP=None, CC=0)
        # self.secs1 = tkVFD.seg7(self, height=vfdHeight, use_CC=True, on_color=onColour, bg=bgColourD)
        # self.secs1.grid(row=0, column=5, padx=(0,0), pady=(0,0))
        # self.secs1.char("8", DP=None, CC=0)

        self.myLogger.debug("  Start of showVFDime bind mouse")
        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.hour0.bind("<Button-1>",        self._startMove)
        self.hour0.bind("<ButtonRelease-1>", self._stopMove)
        self.hour0.bind("<B1-Motion>",       self._moveWindow)

        self.myLogger.debug("  End of showVFDime _createWidgets")

    #  Used to move the app.
    #  Binds start and stop to mouse left click and move to mouse move.
    def _startMove(self, event):
        self.x = event.x
        self.y = event.y

    def _stopMove(self, event):
        self.x = None
        self.y = None

    def _moveWindow(self, event):
        """  Moves the window when the mouse is left clicked and moved.

             When the window is dragged, the mouse moves to the top left hand corner.
             Tried to cure, given up for now.

             The two above methods improve the cursor position, a lot better.
        """
        self.newX = event.x_root - self.x
        self.newY = event.y_root - self.y
        self.main.geometry(f"+{self.newX}+{self.newY}")

    def _timeString(self):
        """  Returns the current time as a text string using the Digit Time time type.
        """
        return self.selectTime.getTime("Digit Time")

    def _update(self):
        """  Updates the main time text.
        """
        timeText = self._timeString()
        self.hour0.char(timeText[0], DP=None, CC=0)
        self.hour1.char(timeText[1], DP=None, CC=1)
        self.mins0.char(timeText[2], DP=None, CC=0)
        self.mins1.char(timeText[3], DP=None, CC=0)
        # self.secs0.char(timeTest[4], DP=None, CC=0)
        # self.secs1.char(timeTest[5], DP=None, CC=1)
        self.after(1000, self._update)






