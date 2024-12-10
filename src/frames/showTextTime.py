###############################################################################################################
#    showTextime   Copyright (C) <2024>  <Kevin Scott>                                                        #
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

import src.selectTime as st


class showTextime(ctk.CTkFrame):
    """  A class that creates the frame for the text time display.

         textTime = showTextime()
         textTime.update() - to update the time and status bar.
    """
    def __init__(self, main, master, myConfig, myLogger):
        super().__init__(main)

        self.main       = main
        self.master     = master
        self.myConfig   = myConfig
        self.myLogger   = myLogger
        self.selectTime = st.SelectTime()
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.onClouur  = self.myConfig.TEXT_ON_COLOUR
        self.offColour = self.myConfig.TEXT_OFF_COLOUR
        self.fgColour  = self.myConfig.BACKGROUND

        self.textFont = ctk.CTkFont(family="Hack", size=26)

        self._createWidgets()

        self.after(1000, self._update)              #  Will update the time.



    def _createWidgets(self):
        """  Create the main time display.
        """
        self.frmRow1 = ctk.CTkFrame(self)
        self.frmRow1.grid(row=0, column=0, sticky="nsw")
        self.firstRow = ["IT", "IS", "E", "TEN", "HALF", "QUARTER", "X"]
        self.firstDic = {}
        for item in self.firstRow:
            self.firstDic[item] = ctk.CTkLabel(self.frmRow1, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.firstDic[item].pack(side=ctk.LEFT)

        self.frmRow2 = ctk.CTkFrame(self)
        self.frmRow2.grid(row=1, column=0, sticky="nsw")
        self.secondRow = ["TWENTY", "FIVE", "ABOUT", "TO", "FEW"]
        self.secondDic = {}
        for item in self.secondRow:
            self.secondDic[item] = ctk.CTkLabel(self.frmRow2, text=item, text_color=self.offColour,
                                                fg_color=self.fgColour, font=self.textFont)
            self.secondDic[item].pack(side=ctk.LEFT)

        self.frmRow3 = ctk.CTkFrame(self)
        self.frmRow3.grid(row=2, column=0, sticky="nsw")
        thirdRow = ["PAST", "ONE", "TWO", "THREE", "v", "FOUR"]
        self.thirdDic = {}
        for item in thirdRow:
            self.thirdDic[item] = ctk.CTkLabel(self.frmRow3, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.thirdDic[item].pack(side=ctk.LEFT)

        self.frmRow4 = ctk.CTkFrame(self)
        self.frmRow4.grid(row=3, column=0, sticky="nsw")
        fourthRow = ["FIVE", "SIX", "SEVEN", "EIGHT", "TEN"]
        self.fourthDic = {}
        for item in fourthRow:
            self.fourthDic[item] = ctk.CTkLabel(self.frmRow4, text=item, text_color=self.offColour,
                                                fg_color=self.fgColour, font=self.textFont)
            self.fourthDic[item].pack(side=ctk.LEFT)

        self.frmRow5 = ctk.CTkFrame(self)
        self.frmRow5.grid(row=4, column=0, sticky="nsw")
        fifthRow = ["NINE", "ELEVEN", "TWELVE", "AS", "HW"]
        self.fifthDic = {}
        for item in fifthRow:
            self.fifthDic[item] = ctk.CTkLabel(self.frmRow5, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.fifthDic[item].pack(side=ctk.LEFT)

        self.frmRow6 = ctk.CTkFrame(self)
        self.frmRow6.grid(row=5, column=0, sticky="nsw")
        sixthRow = ["IN", "XI", "THE", "ON", "AFTER", "NOON", "JC"]
        self.sixthDic = {}
        for item in sixthRow:
            self.sixthDic[item] = ctk.CTkLabel(self.frmRow6, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.sixthDic[item].pack(side=ctk.LEFT)

        self.frmRow7 = ctk.CTkFrame(self)
        self.frmRow7.grid(row=6, column=0, sticky="nsw")
        seventhRow = ["GSIPB", "MORNING", "ZFUP", "BF", "TH"]
        self.seventhDic = {}
        for item in seventhRow:
            self.seventhDic[item] = ctk.CTkLabel(self.frmRow7, text=item, text_color=self.offColour,
                                                 fg_color=self.fgColour, font=self.textFont)
            self.seventhDic[item].pack(side=ctk.LEFT)

        self.frmRow8 = ctk.CTkFrame(self)
        self.frmRow8.grid(row=7, column=0, sticky="nsw")
        eigthRow = ["EVENING", "MOVE", "Z", "MIDNIGHT"]
        self.eigththDic = {}
        for item in eigthRow:
            self.eigththDic[item] = ctk.CTkLabel(self.frmRow8, text=item, text_color=self.offColour,
                                                 fg_color=self.fgColour, font=self.textFont)
            self.eigththDic[item].pack(side=ctk.LEFT)

        #  Bind the top right X to close.
        self.firstDic["X"].bind("<Button-1>",        self._close)
        self.firstDic["X"].configure(text_color="red")

        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.eigththDic["MOVE"].bind("<Button-1>",        self._startMove)
        self.eigththDic["MOVE"].bind("<ButtonRelease-1>", self._stopMove)
        self.eigththDic["MOVE"].bind("<B1-Motion>",       self._moveWindow)
        self.eigththDic["MOVE"].configure(text_color="silver")

    def _close(self, event):
        self.master.update_idletasks()              #  To make sure the app location had been updated.

        self.myConfig.TEXT_X_POS = self.winfo_rootx()
        self.myConfig.TEXT_Y_POS = self.winfo_rooty()

        self.myConfig.writeConfig()

        self.master.state("normal")
        self.master.overrideredirect(True)
        self.main.destroy()

    #  Used to move the app.
    #  Binds start and stop to mouse left click and move to mouse move.
    def _startMove(self, event):
        self.x = event.x
        self.y = event.y
        self.configure(cursor="circle")

    def _stopMove(self, event):
        self.x = None
        self.y = None
        self.configure(cursor="arrow")

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

        # self.after(1000, self._update)






