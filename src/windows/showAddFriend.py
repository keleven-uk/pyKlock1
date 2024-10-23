###############################################################################################################
#    ShowAddFriend.py   Copyright (C) <2024>  <Kevin Scott>                                                   #
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

import tkinter as tk

import customtkinter as ctk
from src.CTkDatePicker import CTkDatePicker
from CTkMessagebox import CTkMessagebox


class FriendAddWindow(ctk.CTkToplevel):
    """  Creates a windows for adding a friend.
         Various text entry fields are used.
         These are then save to a friendStore - detailed else where.

    """
    def __init__(self, master, friendsStore):
        super().__init__(master)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Friends")
        self.geometry("800x480+400+400")
        self.attributes('-topmost', True)
        self.resizable(False, False)

        self.master       = master
        self.friendsStore = friendsStore
        self.titles       = self.friendsStore.getTitles
        self.chosen       = ""

        self._create_widgets()


    def _create_widgets(self):
        """  Create the main add friend frame.
        """
        self.lblTitle = ctk.CTkLabel(self, text="Title", text_color="#ffe9a6", font=("Verdana",20))
        self.lblTitle.grid(row=0, column=0,padx=10, pady=10)
        self.cbxTitle = ctk.CTkComboBox(self, values=self.titles, text_color="white", fg_color="#030126", border_color="#030126", command=self.setTitle)
        self.cbxTitle.grid(row=0, column=1,padx=10, pady=10)

        self.lblFirstName = ctk.CTkLabel(self, text="FirstName", text_color="#ffe9a6", font=("Verdana",20))
        self.lblFirstName.grid(row=1, column=0,padx=10, pady=10)
        self.entFirstName = ctk.CTkEntry(self, placeholder_text="FirstName", text_color="white", fg_color="#030126", border_color="#030126")
        self.entFirstName.grid(row=1, column=1,padx=10, pady=10)

        self.lblLastName = ctk.CTkLabel(self, text="Last Name", text_color="#ffe9a6", font=("Verdana",20))
        self.lblLastName.grid(row=1, column=2,padx=10, pady=10)
        self.entLastName = ctk.CTkEntry(self, placeholder_text="lastName", text_color="white", fg_color="#030126", border_color="#030126")
        self.entLastName.grid(row=1, column=3,padx=10, pady=10)

        self.lblMobileNumber = ctk.CTkLabel(self, text="Mobile Number", text_color="#ffe9a6", font=("Verdana",20))
        self.lblMobileNumber.grid(row=2, column=0,padx=10, pady=10)
        self.entMobileNumber = ctk.CTkEntry(self, placeholder_text="mobileNumber", text_color="white", fg_color="#030126", border_color="#030126")
        self.entMobileNumber.grid(row=2, column=1,padx=10, pady=10)

        self.lblTelNumber = ctk.CTkLabel(self, text="Tel Number", text_color="#ffe9a6", font=("Verdana",20))
        self.lblTelNumber.grid(row=2, column=2,padx=10, pady=10)
        self.entTelNumber = ctk.CTkEntry(self, placeholder_text="Telephone Number", text_color="white", fg_color="#030126", border_color="#030126")
        self.entTelNumber.grid(row=2, column=3,padx=10, pady=10)

        self.lblEmail = ctk.CTkLabel(self, text="E-Mail", text_color="#ffe9a6", font=("Verdana",20))
        self.lblEmail.grid(row=3, column=0,padx=10, pady=10)
        self.entEmail = ctk.CTkEntry(self, placeholder_text="eMail", text_color="white", fg_color="#030126", border_color="#030126")
        self.entEmail.grid(row=3, column=1,padx=10, pady=10)

        self.lblBirthday = ctk.CTkLabel(self, text="Birthday", text_color="#ffe9a6", font=("Verdana",20))
        self.lblBirthday.grid(row=3, column=2,padx=10, pady=10)
        self.dpBirthday = CTkDatePicker(self)
        self.dpBirthday.grid(row=3, column=3,padx=10, pady=10)

        self.dpBirthday.set_date_format("%d/%m/%Y")
        self.dpBirthday.set_allow_manual_input(True)  # Enable


        self.lblHouseNo = ctk.CTkLabel(self, text="House No / Name", text_color="#ffe9a6", font=("Verdana",20))
        self.lblHouseNo.grid(row=4, column=0,padx=10, pady=10)
        self.entHouseNo = ctk.CTkEntry(self, placeholder_text="House no / Name", text_color="white", fg_color="#030126", border_color="#030126")
        self.entHouseNo.grid(row=4, column=1,padx=10, pady=10)

        self.lblAddLine1 = ctk.CTkLabel(self, text="Address Line 1", text_color="#ffe9a6", font=("Verdana",20))
        self.lblAddLine1.grid(row=5, column=0,padx=10, pady=10)
        self.entAddLine1 = ctk.CTkEntry(self, placeholder_text="Address Line 1", text_color="white", fg_color="#030126", border_color="#030126")
        self.entAddLine1.grid(row=5, column=1,padx=10, pady=10)

        self.lblAddLine2 = ctk.CTkLabel(self, text="Address Line 2", text_color="#ffe9a6", font=("Verdana",20))
        self.lblAddLine2.grid(row=5, column=2,padx=10, pady=10)
        self.entAddLine2 = ctk.CTkEntry(self, placeholder_text="Address Line 2", text_color="white", fg_color="#030126", border_color="#030126")
        self.entAddLine2.grid(row=5, column=3,padx=10, pady=10)

        self.lblCity = ctk.CTkLabel(self, text="City", text_color="#ffe9a6", font=("Verdana",20))
        self.lblCity.grid(row=6, column=0,padx=10, pady=10)
        self.entCity = ctk.CTkEntry(self, placeholder_text="City", text_color="white", fg_color="#030126", border_color="#030126")
        self.entCity.grid(row=6, column=1,padx=10, pady=10)

        self.lblCounty = ctk.CTkLabel(self, text="County", text_color="#ffe9a6", font=("Verdana",20))
        self.lblCounty.grid(row=6, column=2,padx=10, pady=10)
        self.entCounty = ctk.CTkEntry(self, placeholder_text="County", text_color="white", fg_color="#030126", border_color="#030126")
        self.entCounty.grid(row=6, column=3,padx=10, pady=10)

        self.lblPostCode = ctk.CTkLabel(self, text="Post Code", text_color="#ffe9a6", font=("Verdana",20))
        self.lblPostCode.grid(row=7, column=0,padx=10, pady=10)
        self.entPostCode = ctk.CTkEntry(self, placeholder_text="Post Code", text_color="white", fg_color="#030126", border_color="#030126")
        self.entPostCode.grid(row=7, column=1,padx=10, pady=10)

        self.lblCountry = ctk.CTkLabel(self, text="Country", text_color="#ffe9a6", font=("Verdana",20))
        self.lblCountry.grid(row=7, column=2,padx=10, pady=10)
        self.entCountry = ctk.CTkEntry(self, placeholder_text="Country", text_color="white", fg_color="#030126", border_color="#030126")
        self.entCountry.grid(row=7, column=3,padx=10, pady=10)


        self.btnAdd = ctk.CTkButton( self, text="Add", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._add)
        self.btnAdd.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")
        self.btnSave = ctk.CTkButton( self, text="Save", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._save, state="disabled")
        self.btnSave.grid(row=9, column=1, padx=10, pady=10, sticky="nsew")
        self.btnExt = ctk.CTkButton( self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._exit)
        self.btnExt.grid(row=9, column=3, padx=10, pady=10, sticky="nsew")


    def setTitle(self, choice):
        """  Saves the choice of the combo box [title] for use elsewhere.
        """
        self.chosen = choice

    def _add(self):
        """  The friendsStore stores the data in a list format access via a key.
             This method created the key and item and calls the friendsStore.add.

             The key = Last Name : First Name
                item = Title, First Name, Last Name, Mobile No, Email, Birthday.

             NB : no validation yet.
        """
        title     = self.chosen
        lastName  = self.entLastName.get().title().strip()
        firstName = self.entFirstName.get().title().strip()
        mobileNo  = self.entMobileNumber.get().strip()
        telNumber = self.entTelNumber.get().strip()
        eMail     = self.entEmail.get().strip()
        birthday  = self.dpBirthday.get_date().strip()
        houseNo   = self.entHouseNo.get().title().strip()
        addLine1  = self.entAddLine1.get().title().strip()
        addLine2  = self.entAddLine2.get().title().strip()
        city      = self.entCity.get().title().strip()
        county    = self.entCounty.get().title().strip()
        postCode  = self.entPostCode.get().upper().strip()
        country   = self.entCountry.get().title().strip()

        if lastName == "" and firstName == "" and mobileNo == "":
            CTkMessagebox(title="Error", message="First, Last Name and Mobile Number are mandatory", icon="cancel")
        else:
            key = f"{lastName} : {firstName}"
            item = [title, lastName, firstName, mobileNo, telNumber, eMail, birthday,
                    houseNo, addLine1, addLine2, city, county, postCode, country]

            self.friendsStore.addFriend(key, item)
            self.btnSave.configure(state="normal")
            self._clear()

    def _save(self):
        """  When called the friends store will save a copy of itself.
             The location and the format of the save is determined in the store.
        """
        self.friendsStore.saveFriends()

    def _edit(self):
        pass

    def _delete(self):
        pass

    def _exit(self):
        """  Closes the window.
        """
        self.destroy()

    def _clear(self):
        """  Clears the text fields [using tk direct].
        """
        self.cbxTitle.set("")
        self.entFirstName.delete(0, tk.END)
        self.entLastName.delete(0, tk.END)
        self.entMobileNumber.delete(0, tk.END)
        self.entEmail.delete(0, tk.END)
        self.dpBirthday.date_entry.delete(0, tk.END)
        self.entHouseNo.delete(0, tk.END)
        self.entAddLine1.delete(0, tk.END)
        self.entAddLine2.delete(0, tk.END)
        self.entCity.delete(0, tk.END)
        self.entCounty.delete(0, tk.END)
        self.entPostCode.delete(0, tk.END)
        self.entCountry.delete(0, tk.END)

        self.cbxTitle.focus()


