###############################################################################################################
#    ShowFriends.py   Copyright (C) <2024>  <Kevin Scott>                                                     #
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

import src.windows.showAddFriend as saf
import src.classes.friendsStore as fs

from CTkMessagebox import CTkMessagebox
from tksheet import Sheet

class FriendsWindow(ctk.CTkToplevel):
    """  A class for adding and showing friends.
    """

    def __init__(self, master, myConfig):
        super().__init__(master)

        self.myConfig         = myConfig
        self.friendsStore     = fs.friendsStore()
        self.master           = master
        self.AddWindowRunning = None

        ctk.set_appearance_mode(self.myConfig.APPEARANCE_MODE)
        ctk.set_default_color_theme(self.myConfig.COLOR_THEME)

        self.title("Friends")
        self.geometry("1010x400+400+400")
        self.resizable(True, False)

        self._createWidgets()

        self.after(60000, self._update)


    def _createWidgets(self):
        """  Create the main friend display.
        """
        self.tblFriends = Sheet(self, data=self.friendsStore.getFriends(), width=1000, height=300,
                                align = "W", header_align = "w", row_index_align = "w",
                                show_x_scrollbar=True, show_y_scrollbar=True)
        self.tblFriends.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=12)
        self.tblFriends.change_theme(self.myConfig.APPEARANCE_MODE)
        self.tblFriends.headers(self.friendsStore.getHeaders)
        self.tblFriends.enable_bindings()
        self.tblFriends.extra_bindings(("row_select", "cell_select"), self.selectRow)

        self.btnAdd = ctk.CTkButton(self, text="Add", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._add)
        self.btnAdd.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.btnEdit = ctk.CTkButton(self, text="Edit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                     corner_radius=12, width=100, state="disabled", command=self._edit)
        self.btnEdit.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.btnDel = ctk.CTkButton(self, text="Delete", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, state="disabled", command=self._delete)
        self.btnDel.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.btnRefresh = ctk.CTkButton(self, text="Refresh", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                        corner_radius=12, width=100, command=self._sheetUpdate)
        self.btnRefresh.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
        self.btnExt = ctk.CTkButton(self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._exit)
        self.btnExt.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

        self._setColumnWidths()

    def _sheetUpdate(self):
        """  Perform the actual sheet update.
        """
        self.tblFriends.set_sheet_data(data=self.friendsStore.getFriends(), redraw=True)
        self._setColumnWidths()

    def _update(self):
        """  The update will run every minute.
             The main purpose it to update the sheet with any new friends,
                if the FriendAddWindow window is running.
        """
        if self.AddWindowRunning is None or not self.AddWindowRunning.winfo_exists():
            self.AddWindowRunning = None
        else:
            self._sheetUpdate()

        self.after(60000, self._update)

    def _setColumnWidths(self):
        self.tblFriends.set_all_column_widths(width=150,   redraw=True)
        self.tblFriends.column_width(column=0,  width=50,  redraw=True)
        self.tblFriends.column_width(column=7,  width=50,  redraw=True)
        self.tblFriends.column_width(column=14, width=300, redraw=True)

    def selectRow(self, event):
        self.btnEdit.configure(state="normal")
        self.btnDel.configure(state="normal")

        rowSelected = self.tblFriends.get_currently_selected()
        rowData     = self.tblFriends.get_row_data(rowSelected[0])
        self.rowKey =  f"{rowData[1]} : {rowData[2]}"

    def _add(self):
        """  Adds a friend to the friend store.
        """
        self.AddWindowRunning = saf.FriendAddWindow(self, self.myConfig, self.friendsStore)

    def _edit(self):
        """  Edits a friend data, displays the updated data.
        """
        if self.rowKey == "":
            CTkMessagebox(title="Error", message="No row selected", icon="cancel")
        else:
            rowSelected = self.tblFriends.get_currently_selected()
            rowData     = self.tblFriends.get_row_data(rowSelected[0])
            self.rowKey =  f"{rowData[1]} : {rowData[2]}"
            self.AddWindowRunning = saf.FriendAddWindow(self, self.myConfig, self.friendsStore, self.rowKey)
            self.rowKey = ""

        self.btnEdit.configure(state="disabled")
        self.btnDel.configure(state="disabled")

    def _delete(self):
        """  Deletes a friend from the store, displays the updated data.
        """
        if self.rowKey == "":
            CTkMessagebox(title="Error", message="No row selected", icon="cancel")
        else:
            msg = CTkMessagebox(title="Delete Friend", message="Do you really want to delete this friend?",
                                icon="question", option_1="Yes", option_2="No")
            if msg.get()=="Yes":
                self.friendsStore.deleteFriend(self.rowKey)
                self.friendsStore.saveFriends()
                self.rowKey = ""
                self._sheetUpdate()

        self.btnEdit.configure(state="disabled")
        self.btnDel.configure(state="disabled")

    def _exit(self):
        """  Closes the window.
        """
        self.destroy()

