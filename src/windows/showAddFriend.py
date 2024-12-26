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

import datetime

import tkinter as tk

from re import compile

import customtkinter as ctk
from tkcalendar    import DateEntry
from CTkMessagebox import CTkMessagebox


class FriendAddWindow(ctk.CTkToplevel):
    """  Creates a windows for adding a friend.
         Various text entry fields are used.
         These are then save to a friendStore - detailed else where.

    """
    def __init__(self, master, myConfig, friendsStore, rowKey=None):
        super().__init__(master)
        self.title("Friends")
        self.geometry("740x580+320+340")
        self.attributes("-topmost", True)
        self.resizable(False, False)

        self.myConfig         = myConfig
        self.friendsStore     = friendsStore
        self.titles           = self.friendsStore.getTitles
        self.rowKey           = rowKey
        self.chosen           = ""
        self.valFirstName     = False
        self.valLastName      = False
        self.valMobileNumber  = False
        self.addData          = False

        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)
        ctk.set_default_color_theme(self.myConfig.COLOUR_THEME)

        self.__createWidgets()
        if self.rowKey:                         #  if rowKey is not None, then in edit mode - load selected friend details into the fields.
            self.__populateFields(self.rowKey)   #  rowkey should hold the row number of the selected friend.
            self.oldKey = self.rowKey           #  Save away, just in case the key is changed.


    def __createWidgets(self):
        """  Create the main add friend frame.
        """
        #  Style for the date entry widget.
        style = tk.ttk.Style()
        style.theme_use("clam")  # -> uncomment this line if the styling does not work

        # Customize the DateEntry style
        style.configure("my.DateEntry",
                        fieldbackground="#030126",      # Background colour of the entry field
                        background="grey",              # Background colour when the dropdown is open
                        foreground="#ffe9a6",           # Text colour in the entry field
                        arrowcolor="white",             # Colour of the dropdown arrow
                        bordercolor="#030126",          # Border colour of the entry field
                        darkcolor="#ffe9a6",            # Colour for dark areas (e.g., arrow borders)
                        lightcolor="#030126",           # Colour for light areas (e.g., arrow background)
                        insertcolor="#030126",          # Colour of the text cursor
                        selectbackground="#030126",     # Background colour of selected text
                        selectforeground="#ffe9a6",     # Text colour of selected text
                        borderwidth=2,
                        locale="en_GB",
                        date_patternstr="%dd/%MM/%Y")

        self.lblTitle = ctk.CTkLabel(self, text="Title", text_color="#ffe9a6", font=("Verdana",20))
        self.lblTitle.grid(row=0, column=0,padx=10, pady=10)
        self.cbxTitle = ctk.CTkComboBox(self, values=self.titles, text_color="white", fg_color="#030126", border_color="#030126", command=self.setTitle)
        self.cbxTitle.grid(row=0, column=1,padx=10, pady=10)

        self.lblFirstName = ctk.CTkLabel(self, text="FirstName", text_color="#ffe9a6", font=("Verdana",20))
        self.lblFirstName.grid(row=1, column=0,padx=10, pady=10)
        self.entFirstName = ctk.CTkEntry(self, placeholder_text="FirstName", text_color="white", fg_color="#030126", border_color="#030126",
                                         validate="focusout", validatecommand=self.__validateFirstName)
        self.entFirstName.grid(row=1, column=1,padx=10, pady=10)

        self.lblLastName = ctk.CTkLabel(self, text="Last Name", text_color="#ffe9a6", font=("Verdana",20))
        self.lblLastName.grid(row=1, column=2,padx=10, pady=10)
        self.entLastName = ctk.CTkEntry(self, placeholder_text="lastName", text_color="white", fg_color="#030126", border_color="#030126",
                                        validate="focusout", validatecommand=self.__validateLastName)
        self.entLastName.grid(row=1, column=3,padx=10, pady=10)

        self.lblMobileNumber = ctk.CTkLabel(self, text="Mobile Number", text_color="#ffe9a6", font=("Verdana",20))
        self.lblMobileNumber.grid(row=2, column=0,padx=10, pady=10)
        self.entMobileNumber = ctk.CTkEntry(self, placeholder_text="mobileNumber", text_color="white", fg_color="#030126", border_color="#030126",
                                            validate="focusout", validatecommand=self.__validateMobileNumber)
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
        self.dpBirthday = DateEntry(self, style="my.DateEntry", width=20)
        self.dpBirthday.grid(row=3, column=3,padx=10, pady=10)

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

        self.lblNotes = ctk.CTkLabel(self, text="Notes", text_color="#ffe9a6", font=("Verdana",20))
        self.lblNotes.grid(row=8, column=0,padx=10, pady=10)
        self.txtNotes = ctk.CTkTextbox(self, width=470, height = 100, text_color="white", fg_color="#030126", border_color="#030126",
                                       corner_radius=10, wrap="word")
        self.txtNotes.grid(row=8, column=1,padx=10, pady=10, columnspan=3)

        self.btnAdd = ctk.CTkButton( self, text="Add", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self.__add, state="disabled")
        self.btnAdd.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")
        self.btnSave = ctk.CTkButton( self, text="Save", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self.__save, state="disabled")
        self.btnSave.grid(row=9, column=1, padx=10, pady=10, sticky="nsew")
        self.btnExt = ctk.CTkButton( self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self.__exit)
        self.btnExt.grid(row=9, column=3, padx=10, pady=10, sticky="nsew")


    def __validateLastName(self):
        """  Validation the Last Name - which is mandatory.

             Must not be blank.
        """
        lastName = self.entLastName.get().title().strip()
        if self.rowKey:
            if lastName != self.friend[1]:
               self.valLastName = True
        else:
            if lastName != "":
               self.valLastName = True

        if self.valFirstName and self.valLastName and self.valMobileNumber:
            self.btnAdd.configure(state="normal")

    def __validateFirstName(self):
        """  Validation the Mobile Number - which is mandatory.

             Must not be blank.
        """
        firstName = self.entFirstName.get().title().strip()
        if self.rowKey:
            if firstName != self.friend[2]:
               self.valFirstName = True
        else:
            if firstName != "":
               self.valFirstName = True

        if self.valFirstName and self.valLastName and self.valMobileNumber:
            self.btnAdd.configure(state="normal")

    def __validateMobileNumber(self):
        """  Validation the Mobile Number - which is mandatory.

             Must not be blank and must be numeric.
        """
        mobileNumber = self.entMobileNumber.get().strip()
        if self.rowKey:
            if mobileNumber != self.friend[3]:
               self.valMobileNumber = True
        else:
            if mobileNumber != "":
               self.valMobileNumber = True

        valMobileNumbers = compile(r"[\d ]")                 #  Only allows digits and spaces.

        if valMobileNumbers.match(mobileNumber):             #  Only allows digits and spaces.
            if self.valFirstName and self.valLastName and self.valMobileNumber:
                self.btnAdd.configure(state="normal")
        else:
            CTkMessagebox(title="Error", message="Mobile Number not numeric", icon="warning")
            self.valMobileNumber = False
            self.entMobileNumber.after_idle(lambda: self.entMobileNumber.configure(validate="focusout"))    #  Reapply validation.

    def setTitle(self, choice):
        """  Saves the choice of the combo box [title] for use elsewhere.
        """
        self.chosen = choice

    def __add(self):
        """  The friendsStore stores the data in a list format access via a key.
             This method created the key and item and calls the friendsStore.add.

             The key = Last Name : First Name
                item = Title, First Name, Last Name, Mobile No, Email, Birthday.

             FirstName and last Name cannot be blank.
             mobileNumber must be numeric [can contain a space].
        """
        title     = self.chosen
        dateDue   = self.dpBirthday.get_date()

        self.lastName  = self.entLastName.get().title().strip()
        self.firstName = self.entFirstName.get().title().strip()
        mobileNo  = self.entMobileNumber.get().strip()
        telNumber = self.entTelNumber.get().strip()
        eMail     = self.entEmail.get().strip()
        birthday  = dateDue.strftime("%d/%m/%Y")
        houseNo   = self.entHouseNo.get().title().strip()
        addLine1  = self.entAddLine1.get().title().strip()
        addLine2  = self.entAddLine2.get().title().strip()
        city      = self.entCity.get().title().strip()
        county    = self.entCounty.get().title().strip()
        postCode  = self.entPostCode.get().upper().strip()
        country   = self.entCountry.get().title().strip()
        notes     = self.txtNotes.get("0.0", "end").strip()                #  return note as entered, extra spaces from the end are removed.

        if self.lastName == "" and self.firstName == "" and mobileNo == "":
            CTkMessagebox(title="Error", message="First, Last Name and Mobile Number are mandatory", icon="cancel")
        else:
            key = f"{self.lastName} : {self.firstName}"
            item = [title, self.lastName, self.firstName, mobileNo, telNumber, eMail, birthday,
                    houseNo, addLine1, addLine2, city, county, postCode, country, notes]

            self.friendsStore.addFriend(key, item)
            self.btnSave.configure(state="normal")
            self.btnAdd.configure(state="disabled")
            self.valFirstName    = False
            self.valLastName     = False
            self.valMobileNumber = False
            self.addData         = True     #  data had been add/edited but not saved.3.12\__setslice__

            self._clear()
            if self.rowKey:
                self._populateFields(self.rowKey)   #  If in edit more, refresh fields.

    def __save(self):
        """  When called the friends store will save a copy of itself.
             The location and the format of the save is determined in the store.
             After save reset class flags adddata and rowKey.
        """
        self.friendsStore.saveFriends()
        if self.addData:
            self.addData = False
        if self.rowKey:
            if self.oldKey != self.rowKey:                      #  The name has changed i.e. the key
                self.eventsStore.deleteEvent(self.oldKey)       #  Delete the original and retain the edited.
            self.rowKey = None

    def __exit(self):
        """  Closes the window.
             Checks whether there is any data to be saved.
             If there is, it asks do you really want to exit, it yes then exit.
             If no, then drop out of the method without doing anything.
             If no data to save [adddata will be false, then exit pyKlock.]
        """
        if self.addData:
            msg = CTkMessagebox(title="Unsaved data", message="Do you really want exit, there is unsaved data?",
                                icon="question", option_1="Yes", option_2="No")
            if msg.get()=="Yes":
                self.destroy()
            else:
                self.__clear()
                self.__populateFields(self.rowKey)      #  If No, then reload the last entered friend.
        else:
            self.destroy()

    def __populateFields(self, rowKey=None):
        """  Populates the data fields with a friend.
             If rowKey is none [not in edit more], then load the last [current] friend.
        """
        if rowKey is None:
            rowKey = f"{self.lastName} : {self.firstName}"  #  if add mode, re-populate using existing data.
        else:
            self.btnAdd.configure(state="normal")      #  If in edit mode, make add button available.

        self.friend = self.friendsStore.getFriend(rowKey)
        self.cbxTitle.set(self.friend[0])
        self.entLastName.insert(0, self.friend[1])
        self.entFirstName.insert(0, self.friend[2])
        self.entMobileNumber.insert(0, self.friend[3])
        self.entTelNumber.insert(0, self.friend[4])
        self.entEmail.insert(0, self.friend[5])
        if self.friend[6]:                                                                    #  Protect against a blank date.
            self.dpBirthday.set_date(datetime.datetime.strptime(self.friend[6], "%d/%m/%Y"))  #  String to datetime)
        else:
            self.dpBirthday.delete(0, "end")
        self.entHouseNo.insert(0, self.friend[7])
        self.entAddLine1.insert(0, self.friend[8])
        self.entAddLine2.insert(0, self.friend[9])
        self.entCity.insert(0, self.friend[10])
        self.entCounty.insert(0, self.friend[11])
        self.entPostCode.insert(0, self.friend[12])
        self.entCountry.insert(0, self.friend[13])
        self.txtNotes.insert("0.0", self.friend[13])

    def __clear(self):
        """  Clears the data fields [using tk direct].
        """
        self.cbxTitle.set("")
        self.entFirstName.delete(0, tk.END)
        self.entLastName.delete(0, tk.END)
        self.entMobileNumber.delete(0, tk.END)
        self.entTelNumber.delete(0, tk.END)
        self.entEmail.delete(0, tk.END)
        self.dpBirthday.set_date(datetime.date.today())       # todays date
        self.entHouseNo.delete(0, tk.END)
        self.entAddLine1.delete(0, tk.END)
        self.entAddLine2.delete(0, tk.END)
        self.entCity.delete(0, tk.END)
        self.entCounty.delete(0, tk.END)
        self.entPostCode.delete(0, tk.END)
        self.entCountry.delete(0, tk.END)
        self.txtNotes.delete("0.0", "end")

        self.cbxTitle.focus()


