###############################################################################################################
#    SelectAddFriends.py   Copyright (C) <2024>  <Kevin Scott>                                                #
#    For changes see history.txt                                                                              #
#                                                                                                             #
#    Colour picker used is from https://github.com/Akascape/CTkColorPicker.                                   #
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

import src.classes.friend as friend


class FriendAddWindow(ctk.CTkToplevel):
    """  A class for choosing colours.
         An external colour picker is launched for the user to select colours.

    """
    def __init__(self, master, myConfig):
        super().__init__(master)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.master = master
        self.title("Friends")
        self.myConfig = myConfig
        self.geometry("800x400+400+400")
        self.attributes('-topmost', True)
        self.resizable(False, False)

        self.chosen  = ""
        self.choices = ["", "Mr", "Ms", "Mrs", "Miss", "Dr"]

        self._create_widgets()


    def _create_widgets(self):
        """  Create the main time display.
        """
        self.lblTitle = ctk.CTkLabel(self, text="Title", text_color="#ffe9a6", font=("Verdana",20))
        self.lblTitle.grid(row=0, column=0,padx=10, pady=10)
        self.cbxTitle = ctk.CTkComboBox(self, values=self.choices, text_color="white", fg_color="#030126", border_color="#030126", command=self.setTitle)
        self.cbxTitle.grid(row=0, column=1,padx=10, pady=10)

        self.lblSurname = ctk.CTkLabel(self, text="Surname", text_color="#ffe9a6", font=("Verdana",20))
        self.lblSurname.grid(row=1, column=0,padx=10, pady=10)
        self.entSurname = ctk.CTkEntry(self, placeholder_text="surname", text_color="white", fg_color="#030126", border_color="#030126")
        self.entSurname.grid(row=1, column=1,padx=10, pady=10)

        self.lblLastName = ctk.CTkLabel(self, text="Last Name", text_color="#ffe9a6", font=("Verdana",20))
        self.lblLastName.grid(row=1, column=2,padx=10, pady=10)
        self.entLastName = ctk.CTkEntry(self, placeholder_text="lastName", text_color="white", fg_color="#030126", border_color="#030126")
        self.entLastName.grid(row=1, column=3,padx=10, pady=10)

        self.lblMobileNumber = ctk.CTkLabel(self, text="Mobile Number", text_color="#ffe9a6", font=("Verdana",20))
        self.lblMobileNumber.grid(row=2, column=0,padx=10, pady=10)
        self.entMobileNumber = ctk.CTkEntry(self, placeholder_text="mobileNumber", text_color="white", fg_color="#030126", border_color="#030126")
        self.entMobileNumber.grid(row=2, column=1,padx=10, pady=10)

        self.lblEmail = ctk.CTkLabel(self, text="E-Mail", text_color="#ffe9a6", font=("Verdana",20))
        self.lblEmail.grid(row=2, column=2,padx=10, pady=10)
        self.entEmail = ctk.CTkEntry(self, placeholder_text="eMail", text_color="white", fg_color="#030126", border_color="#030126")
        self.entEmail.grid(row=2, column=3,padx=10, pady=10)

        self.lblBirthday = ctk.CTkLabel(self, text="Birthday", text_color="#ffe9a6", font=("Verdana",20))
        self.lblBirthday.grid(row=3, column=0,padx=10, pady=10)
        self.entBirthday = ctk.CTkEntry(self, placeholder_text="birthdayl", text_color="white", fg_color="#030126", border_color="#030126")
        self.entBirthday.grid(row=3, column=1,padx=10, pady=10)

        self.btnAdd = ctk.CTkButton( self, text="Add", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._add)
        self.btnAdd.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        # self.btnEdit = ctk.CTkButton( self, text="Edit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
        #                             corner_radius=12, width=100, command=self._edit)
        # self.btnEdit.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        # self.btnDel = ctk.CTkButton( self, text="Delete", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
        #                             corner_radius=12, width=100, command=self._delete)
        # self.btnDel.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.btnExt = ctk.CTkButton( self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._exit)
        self.btnExt.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")


    def setTitle(self, choice):
        self.chosen = choice

    def _add(self):
        newFriend = friend.Friend(self.Chosen,
                                  entSurname.get(),
                                  entLastName.get(),
                                  entMobileNumber.get(),
                                  entEmail.get(),
                                  entBirthday.get(),
                                  "")

    def _edit(self):
        pass

    def _delete(self):
        pass

    def _exit(self):
        """  Closes the window.
        """
        self.master.destroy()

