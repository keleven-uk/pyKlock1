###############################################################################################################
#    events.py   Copyright (C) <2024>  <Kevin Scott>                                                          #
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

import CTkColorPicker as ctk_cp

class MyEventsFrame(ctk.CTkFrame):
    """  A class that creates a frame that holds the user settings for Events.

         The three stage days entry fields will only accept decimal numbers.

        Note : this frame uses a copy of the Config file i.e. not config.
    """
    def __init__(self, master, main, config):
        super().__init__(main)

        self.master     = master
        self.main       = main
        self.config     = config
        self.foreColour = "white"

        self.__createWidgets()


    def __createWidgets(self):
        """  Create the main frame.
        """
        self.configure(fg_color=self.config.BACKGROUND)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(3, weight=2)
        self.lblTitle = ctk.CTkLabel(self, text="Events Settings", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblTitle.grid(row=0, column=2)
        #---------------------------------------------------------------------------------------------- stage 1 ----------------------
        self.lblStage1Days = ctk.CTkLabel(self, text="Stage 1 Days", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblStage1Days.grid(row=1, column=0, padx=10, pady=10, sticky="news")
        self.entStage1Days = ctk.CTkEntry(self, placeholder_text=self.config.EVENTS_STAGE_1_DAYS, width=50,
                                          text_color=self.foreColour, fg_color="#030126", border_color=self.foreColour,
                                          validate="focusout", validatecommand=(self.register(self.__validateStageDays), "%P", "1"))
        self.entStage1Days.grid(row=1, column=1,padx=10, pady=10)
        self.lblStage1Colour = ctk.CTkLabel(self, text="Stage 1 Colour", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblStage1Colour.grid(row=1, column=2, padx=10, pady=10, sticky="news")
        self.btnStage1Colour = ctk.CTkButton(self, text="", command=self.__askStage1Colour,
                                           fg_color=self.config.EVENTS_STAGE_1_COLOUR, hover_color="gray",
                                           corner_radius=12, width=100, text_color=self.foreColour,
                                           font=("Montserrat", 16))
        self.btnStage1Colour.grid(row=1, column=3, padx=10, pady=10, sticky="news")
        #---------------------------------------------------------------------------------------------- stage 2 ----------------------
        self.lblStage2Days = ctk.CTkLabel(self, text="Stage 2 Days", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblStage2Days.grid(row=2, column=0, padx=10, pady=10, sticky="news")
        self.entStage2Days = ctk.CTkEntry(self, placeholder_text=self.config.EVENTS_STAGE_2_DAYS, width=50,
                                          text_color=self.foreColour, fg_color="#030126", border_color=self.foreColour,
                                          validate="focusout", validatecommand=(self.register(self.__validateStageDays), "%P", "2"))
        self.entStage2Days.grid(row=2, column=1,padx=10, pady=10)
        self.lblStage2Colour = ctk.CTkLabel(self, text="Stage 2 Colour", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblStage2Colour.grid(row=2, column=2, padx=10, pady=10, sticky="news")
        self.btnStage2Colour = ctk.CTkButton(self, text="", command=self.__askStage2Colour,
                                           fg_color=self.config.EVENTS_STAGE_2_COLOUR, hover_color="gray",
                                           corner_radius=12, width=100, text_color=self.foreColour,
                                           font=("Montserrat", 16))
        self.btnStage2Colour.grid(row=2, column=3, padx=10, pady=10, sticky="news")
        #---------------------------------------------------------------------------------------------- stage 3 ----------------------
        self.lblStage3Days = ctk.CTkLabel(self, text="Stage 3 Days", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblStage3Days.grid(row=3, column=0, padx=10, pady=10, sticky="news")
        self.entStage3Days = ctk.CTkEntry(self, placeholder_text=self.config.EVENTS_STAGE_3_DAYS, width=50,
                                          text_color=self.foreColour, fg_color="#030126", border_color=self.foreColour,
                                          validate="focusout", validatecommand=(self.register(self.__validateStageDays), "%P", "3"))
        self.entStage3Days.grid(row=3, column=1,padx=10, pady=10)
        self.lblStage3Colour = ctk.CTkLabel(self, text="Stage 3 Colour", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblStage3Colour.grid(row=3, column=2, padx=10, pady=10, sticky="news")
        self.btnStage3Colour = ctk.CTkButton(self, text="", command=self.__askStage3Colour,
                                           fg_color=self.config.EVENTS_STAGE_3_COLOUR, hover_color="gray",
                                           corner_radius=12, width=100, text_color=self.foreColour,
                                           font=("Montserrat", 16))
        self.btnStage3Colour.grid(row=3, column=3, padx=10, pady=10, sticky="news")
        #---------------------------------------------------------------------------------------------- Due Now ----------------------
        self.lblDueNowColour = ctk.CTkLabel(self, text="Due Now Colour", text_color=self.foreColour,
                                         fg_color=self.config.BACKGROUND)
        self.lblDueNowColour.grid(row=4, column=2, padx=10, pady=10, sticky="news")
        self.btnDueNowColour = ctk.CTkButton(self, text="", command=self.__askDueNowColour,
                                           fg_color=self.config.EVENTS_NOW_COLOUR, hover_color="gray",
                                           corner_radius=12, width=100, text_color=self.foreColour,
                                           font=("Montserrat", 16))
        self.btnDueNowColour.grid(row=4, column=3, padx=10, pady=10, sticky="news")


    def __validateStageDays(self, data, stage):
        """  Stage days has to be an integer number.
             The validation checks this and allows decimal numbers.
             This is called by all three stage days entry fields.
        """
        print("__validateStageDay")
        valid = data.isdecimal()
        print(f"valid = {valid} {data}")
        if valid:
            match stage:
                case "1":
                    self.config.EVENTS_STAGE_1_DAYS = data
                case "2":
                    self.config.EVENTS_STAGE_2_DAYS = data
                case "3":
                    self.config.EVENTS_STAGE_3_DAYS = data

        return valid

    def __askStage1Colour(self):
        """  Sets the the colour for stage 1.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                    # open the colour picker
        self.config.EVENTS_STAGE_1_COLOUR = pickColor.get()                              # get the colour string
        self.btnStage1Colour.configure(fg_color=self.config.EVENTS_STAGE_1_COLOUR)

    def __askStage2Colour(self):
        """  Sets the the colour for stage 2.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                    # open the colour picker
        self.config.EVENTS_STAGE_2_COLOUR = pickColor.get()                              # get the colour string
        self.btnStage2Colour.configure(fg_color=self.config.EVENTS_STAGE_2_COLOUR)

    def __askStage3Colour(self):
        """  Sets the the colour for stage 3.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                    # open the colour picker
        self.config.EVENTS_STAGE_3_COLOUR = pickColor.get()                              # get the colour string
        self.btnStage3Colour.configure(fg_color=self.config.EVENTS_STAGE_3_COLOUR)

    def __askDueNowColour(self):
        """  Sets the the colour for evets due now.
        """
        self.master.btnSave.configure(state="normal")
        pickColor = ctk_cp.AskColor()                                                    # open the colour picker
        self.config.EVENTS_NOW_COLOUR = pickColor.get()                              # get the colour string
        self.btnDueNowColour.configure(fg_color=self.config.EVENTS_NOW_COLOUR)
