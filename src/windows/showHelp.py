###############################################################################################################
#    showHelp.py   Copyright (C) <2024>  <Kevin Scott>                                                        #
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
import src.CTkPDFViewer as ctkPDF

from src.projectPaths import HELP_PATH


class showHelp(ctk.CTkToplevel):
    """  A class to display Klock's help file in pdf format.
    """
    def __init__(self, master):
        super().__init__(master)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("700x600")
        self.title("Klock Help")

        pdfFrame = ctkPDF.CTkPDFViewer(self, file=f"{HELP_PATH}\\Klock.pdf")
        pdfFrame.pack(fill="both", expand=True, padx=10, pady=10)