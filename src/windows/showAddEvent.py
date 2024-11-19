###############################################################################################################
#    ShowAddEvent.py   Copyright (C) <2024>  <Kevin Scott>                                                   #
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


class EventAddWindow(ctk.CTkToplevel):
    """  Creates a windows for adding a event.
         Various text entry fields are used.
         These are then save to a eventStore - detailed else where.

    """
    def __init__(self, master, myConfig, eventsStore, rowKey=None):
        super().__init__(master)
        self.title("Events")
        self.geometry("700x300+320+340")
        self.attributes("-topmost", True)
        self.resizable(False, False)

        self.myConfig    = myConfig
        self.eventsStore = eventsStore
        self.Categories  = self.eventsStore.getCategories
        self.rowKey      = rowKey
        self.chosen      = ""
        self.valName     = False
        self.addData     = False

        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)
        ctk.set_default_color_theme(self.myConfig.COLOR_THEME)

        self._createWidgets()
        if self.rowKey:                         #  if rowKey is not None, then in edit mode - load selected event details into the fields.
            self._populateFields(self.rowKey)   #  rowkey should hold the row number of the selected event.


    def _createWidgets(self):
        """  Create the main add event frame.
        """
        self.lblName = ctk.CTkLabel(self, text="Name", text_color="#ffe9a6", font=("Verdana",20))
        self.lblName.grid(row=0, column=0,padx=10, pady=10)
        self.entName = ctk.CTkEntry(self, placeholder_text="Event Name", text_color="white", fg_color="#030126", border_color="#030126",
                                         validate="focusout", validatecommand=self._validateName)
        self.entName.grid(row=0, column=1,padx=10, pady=10)

        self.lblCategory = ctk.CTkLabel(self, text="Category", text_color="#ffe9a6", font=("Verdana",20))
        self.lblCategory.grid(row=0, column=2,padx=10, pady=10)
        self.cbxCategory = ctk.CTkComboBox(self, values=self.Categories, text_color="white", fg_color="#030126", border_color="#030126", command=self.setCategory)
        self.cbxCategory.grid(row=0, column=3,padx=10, pady=10)

        self.lblDateDue = ctk.CTkLabel(self, text="Date Due", text_color="#ffe9a6", font=("Verdana",20))
        self.lblDateDue.grid(row=3, column=0,padx=10, pady=10)
        self.dpDateDue = CTkDatePicker(self)
        self.dpDateDue.grid(row=3, column=1,padx=10, pady=10)

        self.dpDateDue.set_date_format("%d/%m/%Y")
        self.dpDateDue.set_allow_manual_input(True)  # Enable


        self.lblNotes = ctk.CTkLabel(self, text="Notes", text_color="#ffe9a6", font=("Verdana",20))
        self.lblNotes.grid(row=8, column=0,padx=10, pady=10)
        self.txtNotes = ctk.CTkTextbox(self, width=470, height = 100, text_color="white", fg_color="#030126", border_color="#030126",
                                       corner_radius=10, wrap="word")
        self.txtNotes.grid(row=8, column=1,padx=10, pady=10, columnspan=3)


        self.btnAdd = ctk.CTkButton( self, text="Add", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._add, state="disabled")
        self.btnAdd.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")
        self.btnSave = ctk.CTkButton( self, text="Save", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._save, state="disabled")
        self.btnSave.grid(row=9, column=1, padx=10, pady=10, sticky="nsew")
        self.btnExt = ctk.CTkButton( self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._exit)
        self.btnExt.grid(row=9, column=3, padx=10, pady=10, sticky="nsew")


    def _validateName(self):
        """  Validation the Name - which is mandatory.

             Must not be blank.
        """
        name = self.entName.get().title().strip()
        if self.rowKey:                 #  In edit mode
            if name != self.event[1]:
               self.valName = True
        else:                           #  In add mode.
            if name != "":
               self.valName = True

        if self.valName:
            self.btnAdd.configure(state="normal")

    def setCategory(self, choice):
        """  Saves the choice of the combo box [title] for use elsewhere.
        """
        self.chosen = choice

    def _add(self):
        """  The eventsStore stores the data in a list format access via a key.
             This method created the key and item and calls the eventsStore.add.

             The key = Last Name : First Name
                item = Title, First Name, Last Name, Mobile No, Email, Birthday.

             FirstName and last Name cannot be blank.
             mobileNumber must be numeric [can contain a space].
        """
        Category  = self.chosen
        name      = self.entName.get().title().strip()
        dateDue   = self.dpDateDue.get_date().strip()
        notes     = self.txtNotes.get("0.0", "end").strip()                #  return note as entered, extra spaces from the end are removed.

        if name == "":
            CTkMessagebox(title="Error", message="Name is mandatory", icon="cancel")
        else:
            key = f"{name}"
            item = [name, dateDue, "00:00", Category, notes]

            self.eventsStore.addEvent(key, item)
            self.btnSave.configure(state="normal")
            self.btnAdd.configure(state="disabled")
            self.valName = False
            self.addData = True     #  data had been add/edited but not saved.

            self._clear()
            if self.rowKey:
                self._populateFields(self.rowKey)   #  If in edit more, refresh fields.

    def _save(self):
        """  When called the events store will save a copy of itself.
             The location and the format of the save is determined in the store.
             After save reset class flags adddata and rowKey.
        """
        self.eventsStore.saveEvents()
        if self.addData:
            self.addData = False
        if self.rowKey:
            self.rowKey = None

    def _exit(self):
        """  Closes the window.
             Checks whether there is any data to be saved.
             If there is, it asks do you really want to exit, it yes then exit.
             If no, then drop out of the method without doing anything.
             If no data to save [adddata will be false, then exit Klock.]
        """
        if self.addData:
            msg = CTkMessagebox(title="Unsaved data", message="Do you really want exit, there is unsaved data?",
                                icon="question", option_1="Yes", option_2="No")
            if msg.get()=="Yes":
                self.destroy()
            else:
                self._clear()
                self._populateFields(self.rowKey)      #  If No, then reload the last entered event.
        else:
            self.destroy()

    def _populateFields(self, rowKey=None):
        """  Populates the data fields with a event.
             If rowKey is none [not in edit more], then load the last [current] event.
        """
        if rowKey is None:
            rowKey = f"{self.Name}"                             #  if add mode, re-populate using existing data.
        else:
            self.btnAdd.configure(state="normal")               #  If in edit mode, make add button available.

        self.event = self.eventsStore.getevent(rowKey)
        self.cbxCategory.set(self.event[0])
        self.Name.insert(0, self.event[1])
        self.dpDateDue.date_entry.insert(0, self.event[2])      #  Accessing date picker internals directly.
        self.txtNotes.insert("0.0", self.event[3])

    def _clear(self):
        """  Clears the data fields [using tk direct].
        """
        self.cbxCategory.set("")
        self.entName.delete(0, tk.END)
        self.dpDateDue.date_entry.delete(0, tk.END)
        self.txtNotes.delete("0.0", "end")

        self.entName.focus()


