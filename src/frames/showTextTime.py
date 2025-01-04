###############################################################################################################
#    showTextime   Copyright (C) <2024-25>  <Kevin Scott>                                                     #
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
        self.onColour   = self.myConfig.TEXTKLOCK_ON_COLOUR
        self.offColour  = self.myConfig.TEXTKLOCK_OFF_COLOUR
        self.fgColour   = self.myConfig.BACKGROUND

        self.textFont = ctk.CTkFont(family="Hack", size=26)

        self.__createWidgets()

        self.after(1000, self.__update)              #  Will update the time.



    def __createWidgets(self):
        """  Create the main time display.
        """
        self.frmRow1 = ctk.CTkFrame(self)
        self.frmRow1.grid(row=0, column=0, sticky="nsw")
        self.firstRow = ["IT", "EE", "IS", "K", "A", "TEN", "HALF", "QUARTER", "I", "X"]
        self.firstDic = {}
        for item in self.firstRow:
            self.firstDic[item] = ctk.CTkLabel(self.frmRow1, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.firstDic[item].pack(side=ctk.LEFT)

        self.frmRow2 = ctk.CTkFrame(self)
        self.frmRow2.grid(row=1, column=0, sticky="nsw")
        self.secondRow = ["TWENTY", "K", "FIVE", "J", "ABOUT", "P", "TO", "S", "FEW"]
        self.secondDic = {}
        for item in self.secondRow:
            self.secondDic[item] = ctk.CTkLabel(self.frmRow2, text=item, text_color=self.offColour,
                                                fg_color=self.fgColour, font=self.textFont)
            self.secondDic[item].pack(side=ctk.LEFT)

        self.frmRow3 = ctk.CTkFrame(self)
        self.frmRow3.grid(row=2, column=0, sticky="nsw")
        thirdRow = ["PAST", "K","ONE", "L", "TWO", "O", "THREE", "C", "FOUR", "K"]
        self.thirdDic = {}
        for item in thirdRow:
            self.thirdDic[item] = ctk.CTkLabel(self.frmRow3, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.thirdDic[item].pack(side=ctk.LEFT)

        self.frmRow4 = ctk.CTkFrame(self)
        self.frmRow4.grid(row=3, column=0, sticky="nsw")
        fourthRow = ["FIVE", "D", "SIX", "U", "SEVEN", "R", "EIGHT", "M", "TEN"]
        self.fourthDic = {}
        for item in fourthRow:
            self.fourthDic[item] = ctk.CTkLabel(self.frmRow4, text=item, text_color=self.offColour,
                                                fg_color=self.fgColour, font=self.textFont)
            self.fourthDic[item].pack(side=ctk.LEFT)

        self.frmRow5 = ctk.CTkFrame(self)
        self.frmRow5.grid(row=4, column=0, sticky="nsw")
        fifthRow = ["NINE", "K", "ELEVEN", "U", "TWELVE", "TAS", "HOW"]
        self.fifthDic = {}
        for item in fifthRow:
            self.fifthDic[item] = ctk.CTkLabel(self.frmRow5, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.fifthDic[item].pack(side=ctk.LEFT)

        self.frmRow6 = ctk.CTkFrame(self)
        self.frmRow6.grid(row=5, column=0, sticky="nsw")
        sixthRow = ["IN", "XIN", "THE", "L", "ON", "I", "AFTER", "NOON", "T", "JC"]
        self.sixthDic = {}
        for item in sixthRow:
            self.sixthDic[item] = ctk.CTkLabel(self.frmRow6, text=item, text_color=self.offColour,
                                               fg_color=self.fgColour, font=self.textFont)
            self.sixthDic[item].pack(side=ctk.LEFT)

        self.frmRow7 = ctk.CTkFrame(self)
        self.frmRow7.grid(row=6, column=0, sticky="nsw")
        seventhRow = ["GSIPB", "O", "MORNING", "Q","ZFUP", "G", "BF", "OTH"]
        self.seventhDic = {}
        for item in seventhRow:
            self.seventhDic[item] = ctk.CTkLabel(self.frmRow7, text=item, text_color=self.offColour,
                                                 fg_color=self.fgColour, font=self.textFont)
            self.seventhDic[item].pack(side=ctk.LEFT)

        self.frmRow8 = ctk.CTkFrame(self)
        self.frmRow8.grid(row=7, column=0, sticky="nsw")
        eighthRow = ["EVENING", "N", "MOVE", "A", "XZX", "MIDNIGHT"]
        self.eighthDic = {}
        for item in eighthRow:
            self.eighthDic[item] = ctk.CTkLabel(self.frmRow8, text=item, text_color=self.offColour,
                                                 fg_color=self.fgColour, font=self.textFont)
            self.eighthDic[item].pack(side=ctk.LEFT)

        #  Bind the top right X to close.
        self.firstDic["X"].bind("<Button-1>", self.__close)

        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.eighthDic["MOVE"].bind("<Button-1>",        self.__startMove)
        self.eighthDic["MOVE"].bind("<ButtonRelease-1>", self.__stopMove)
        self.eighthDic["MOVE"].bind("<B1-Motion>",       self.__moveWindow)
        self.eighthDic["MOVE"].configure(text_color="silver")

    def __close(self, event):
        self.master.update_idletasks()              #  To make sure the app location had been updated.

        self.myConfig.TEXTKLOCK_X_POS = self.winfo_rootx()
        self.myConfig.TEXTKLOCK_Y_POS = self.winfo_rooty()

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

    def __setHours(self, hours, minutes):
        """  Switches on the appropriate text to display the hour.
        """
        self.firstDic["IT"].configure(text_color=self.onColour)
        self.firstDic["IS"].configure(text_color=self.onColour)
        self.sixthDic["IN"].configure(text_color=self.onColour)
        self.sixthDic["THE"].configure(text_color=self.onColour)

        if minutes > 30:     #  Increment hours if time is close to the hour.
            hours += 1

        match hours:
            case 0 | 24:
                if minutes in [58, 59, 0, 1]:
                    self.eighthDic["MIDNIGHT"].configure(text_color=self.onColour)
                    self.sixthDic["IN"].configure(text_color=self.offColour)
                    self.sixthDic["THE"].configure(text_color=self.offColour)
                else:
                    self.fifthDic["TWELVE"].configure(text_color=self.onColour)
                    if minutes > 30:
                        self.eighthDic["EVENING"].configure(text_color=self.onColour)
                    else:
                        self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 1:
                self.thirdDic["ONE"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 2:
                self.thirdDic["TWO"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 3:
                self.thirdDic["THREE"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 4:
                self.thirdDic["FOUR"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 5:
                self.fourthDic["FIVE"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 6:
                self.fourthDic["SIX"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 7:
                self.fourthDic["SEVEN"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 8:
                self.fourthDic["EIGHT"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 9:
                self.fifthDic["NINE"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 10:
                self.fourthDic["TEN"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 11:
                self.fifthDic["ELEVEN"].configure(text_color=self.onColour)
                self.seventhDic["MORNING"].configure(text_color=self.onColour)
            case 12:
                if minutes in [58, 59, 0, 1]:
                    self.sixthDic["NOON"].configure(text_color=self.onColour)
                    self.sixthDic["IN"].configure(text_color=self.offColour)
                    self.sixthDic["THE"].configure(text_color=self.offColour)
                else:
                    self.fifthDic["TWELVE"].configure(text_color=self.onColour)
                    if minutes >30:
                        self.seventhDic["MORNING"].configure(text_color=self.onColour)
                    else:
                        self.sixthDic["AFTER"].configure(text_color=self.onColour)
                        self.sixthDic["NOON"].configure(text_color=self.onColour)
            case 13:
                self.thirdDic["ONE"].configure(text_color=self.onColour)
                self.sixthDic["AFTER"].configure(text_color=self.onColour)
                self.sixthDic["NOON"].configure(text_color=self.onColour)
            case 14:
                self.thirdDic["TWO"].configure(text_color=self.onColour)
                self.sixthDic["AFTER"].configure(text_color=self.onColour)
                self.sixthDic["NOON"].configure(text_color=self.onColour)
            case 15:
                self.thirdDic["THREE"].configure(text_color=self.onColour)
                self.sixthDic["AFTER"].configure(text_color=self.onColour)
                self.sixthDic["NOON"].configure(text_color=self.onColour)
            case 16:
                self.thirdDic["FOUR"].configure(text_color=self.onColour)
                self.sixthDic["AFTER"].configure(text_color=self.onColour)
                self.sixthDic["NOON"].configure(text_color=self.onColour)
            case 17:
                self.fourthDic["FIVE"].configure(text_color=self.onColour)
                self.sixthDic["AFTER"].configure(text_color=self.onColour)
                self.sixthDic["NOON"].configure(text_color=self.onColour)
            case 18:
                self.fourthDic["SIX"].configure(text_color=self.onColour)
                self.eighthDic["EVENING"].configure(text_color=self.onColour)
            case 19:
                self.fourthDic["SEVEN"].configure(text_color=self.onColour)
                self.eighthDic["EVENING"].configure(text_color=self.onColour)
            case 20:
                self.fourthDic["EIGHT"].configure(text_color=self.onColour)
                self.eighthDic["EVENING"].configure(text_color=self.onColour)
            case 21:
                self.fifthDic["NINE"].configure(text_color=self.onColour)
                self.eighthDic["EVENING"].configure(text_color=self.onColour)
            case 22:
                self.fourthDic["TEN"].configure(text_color=self.onColour)
                self.eighthDic["EVENING"].configure(text_color=self.onColour)
            case 23:
                self.fifthDic["ELEVEN"].configure(text_color=self.onColour)
                self.eighthDic["EVENING"].configure(text_color=self.onColour)

    def __setMinutes(self, minutes):
        """  Switches on the appropriate text to display the minutes.
        """
        if minutes > 30:
            minutes = 60 - minutes
            self.secondDic["TO"].configure(text_color=self.onColour)
        else:
            self.thirdDic["PAST"].configure(text_color=self.onColour)

        match minutes:
            case minutes if (0 <= minutes <= 2):
                self.secondDic["TO"].configure(text_color=self.offColour)
                self.thirdDic["PAST"].configure(text_color=self.offColour)
            case minutes if (2 < minutes <= 7):
                self.secondDic["FIVE"].configure(text_color=self.onColour)
            case minutes if (7 < minutes <= 12):
                self.firstDic["TEN"].configure(text_color=self.onColour)
            case minutes if (13 < minutes <= 17):
                self.firstDic["A"].configure(text_color=self.onColour)
                self.firstDic["QUARTER"].configure(text_color=self.onColour)
            case minutes if (17 < minutes <= 22):
                self.secondDic["TWENTY"].configure(text_color=self.onColour)
            case minutes if (22 < minutes <= 27):
                self.secondDic["TWENTY"].configure(text_color=self.onColour)
                self.secondDic["FIVE"].configure(text_color=self.onColour)
            case minutes if (27 < minutes <= 30):
                self.secondDic["TO"].configure(text_color=self.offColour)
                self.thirdDic["PAST"].configure(text_color=self.onColour)
                self.firstDic["HALF"].configure(text_color=self.onColour)

    def __clear(self):
        """  Switches off all texts.
        """
        for item in self.firstDic:
            self.firstDic[item].configure(text_color=self.offColour)

        for item in self.secondDic:
            self.secondDic[item].configure(text_color=self.offColour)

        for item in self.thirdDic:
            self.thirdDic[item].configure(text_color=self.offColour)

        for item in self.fourthDic:
            self.fourthDic[item].configure(text_color=self.offColour)

        for item in self.fifthDic:
            self.fifthDic[item].configure(text_color=self.offColour)

        for item in self.sixthDic:
            self.sixthDic[item].configure(text_color=self.offColour)

        for item in self.seventhDic:
            self.seventhDic[item].configure(text_color=self.offColour)

        for item in self.eighthDic:
            self.eighthDic[item].configure(text_color=self.offColour)

        self.eighthDic["MOVE"].configure(text_color="silver")           #  Switch on the X in the top right corner [exit button]
        self.firstDic["X"].configure(text_color="red")                  #  Switch on the MOVE text [move button]

    def __update(self):
        """  Updates the main time text.
        """
        self.__clear()
        timeText = self.selectTime.getTime("Local Time")
        hours    = int(timeText[0:2])
        minutes  = int(timeText[3:5])

        self.__setHours(hours, minutes)
        self.__setMinutes(minutes)

        self.after(60000, self.__update)                                #  Update every minute.






