###############################################################################################################
#    showMainTime   Copyright (C) <2024-25>  <Kevin Scott>                                                    #
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
import src.utils.klock_utils as utils

class MyMainTimeFrame(ctk.CTkFrame):
    """  A class that creates the frame for the main time display.

         mt = MyMainTimeFrame()
         mt.update() - to update the main time colours.
    """
    def __init__(self, main, myConfig):
        super().__init__(main)

        self.main   = main
        self.myConfig = myConfig
        self.selectTime = st.SelectTime()
        self.timeFont = ctk.CTkFont(family=self.myConfig.TIME_FONT_FAMILY, size=self.myConfig.TIME_FONT_SIZE)
        self.screenWidth, self.screenHeight = utils.getScreenSize()
        self.newY = self.myConfig.Y_POS
        self.__createWidgets()
        self.update()


    def __createWidgets(self):
        """  Create the main time display.
        """
        self.configure(fg_color=self.myConfig.BACKGROUND)
        self.lblTime = ctk.CTkLabel(self, text=self.__timeString(), font=self.timeFont,
                                    text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND)
        self.lblTime.pack(expand=True)

        #  Using tkinter direct to bind the move window function to the left moue button press.
        self.lblTime.bind("<Button-1>",        self.__startMove)
        self.lblTime.bind("<ButtonRelease-1>", self.__stopMove)
        self.lblTime.bind("<B1-Motion>",       self.__moveWindow)

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
        """  Returns the current time as a text string using the current time type.

             If required, will return the time string capitalised.
        """
        if self.myConfig.TIME_CAPITALISE:
            return self.selectTime.getTime(self.myConfig.TIME_TYPE).capitalize()
        else:
            return self.selectTime.getTime(self.myConfig.TIME_TYPE)


    def update(self):
        """  Updates the main time text.
             The method updates both text and font.
             Method is externally called.
             The length of the new time test is determined and used to resize the window so the text fits,
             Also the window is positioned right aligned to the screen, if configured.

             TODO : Maybe a choice of left alignment.
        """
        self.timeFont.configure(family=self.myConfig.TIME_FONT_FAMILY, size=self.myConfig.TIME_FONT_SIZE)   #  Change font if required.

        timeTest = self.__timeString()
        newW = self.timeFont.measure(text=timeTest)                                                         #  Get the length, in pixels, of  the time text

        if newW < self.myConfig.WIN_WIDTH:                                                                  #  Keep a minimum window width.
            newW = self.myConfig.WIN_WIDTH

        if self.myConfig.ALIGN_RIGHT:                                                                       #  Only change x position of window, if required.
            self.newX = self.screenWidth - newW - 20                                                        #  Find the position of the window right justified to the screen

        self.main.geometry(f"{newW}x{self.myConfig.WIN_HEIGHT}+{self.newX}+{self.newY}")                    #  Dynamically sets the main window to fit.
                                                                                                            #  [Don't change the windows Y position]

        self.lblTime.configure(text=timeTest, text_color=self.myConfig.FOREGROUND, fg_color=self.myConfig.BACKGROUND, font=self.timeFont)






