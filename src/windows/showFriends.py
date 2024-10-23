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

import src.CTkXYFrame as CTkXY
import src.windows.showAddFriend as saf
import src.classes.friendsStore as fs

from tksheet import Sheet

class FriendsWindow(ctk.CTkToplevel):
    """  A class for adding and showing friends.
    """

    def __init__(self, master, myConfig):
        super().__init__(master)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.myConfig     = myConfig
        self.friendsStore = fs.friendsStore()
        self.master       = master

        self.title("Friends")
        self.geometry("1000x400+400+400")
        self.resizable(False, False)

        self._create_widgets()

        self.after(60000, self._update)


    def _create_widgets(self):
        """  Create the main friend display.
        """
        self.tf = topFrame(self, self.friendsStore)
        self.tf.pack(padx=10, pady=10, fill="both", expand=True)
        self.bf = ButtonFrame(self, self.friendsStore)
        self.bf.pack(padx=10, pady=10)

    def _update(self):
        """  The update will run every minute.
             The main purpose it to update the top frame with any new friends,
                if the FriendAddWindow window is running.
        """
        if self.bf.AddWindowRunning is None or not self.bf.AddWindowRunning.winfo_exists():
            self.bf.AddWindowRunning = None
        else:
            self.tf.update()
        self.after(60000, self._update)


class topFrame(CTkXY.CTkXYFrame):
    """  A class for the top form of the friends window.
         The friends display.
    """
    def __init__(self, master, friendsStore):
        super().__init__(master)

        self.friendsStore = friendsStore
        self._create_widgets()

    def _create_widgets(self):

        self.tblFriends = Sheet(self, data=self.friendsStore.getFriends(), width=1900, height=300,
                                align = "W", header_align = "w", row_index_align = "w",
                                show_x_scrollbar=False, show_y_scrollbar=False)
        self.tblFriends.pack(expand=True, fill="both")
        self.tblFriends.change_theme("dark")
        self.tblFriends.headers(self.friendsStore.getHeaders)
        self._setColumnWidths()

    def _setColumnWidths(self):
        self.tblFriends.set_all_column_widths(width=150, redraw=True)
        self.tblFriends.column_width(column=0, width=50, redraw=True)
        self.tblFriends.column_width(column=7, width=50, redraw=True)

    def update(self):
        self.tblFriends.set_sheet_data(data=self.friendsStore.getFriends(), redraw=True)
        self._setColumnWidths()


class ButtonFrame(ctk.CTkFrame):
    """  A class to display the buttons.
    """
    def __init__(self, master, friendsStore):
        super().__init__(master)

        self.master           = master
        self.friendsStore     = friendsStore
        self.AddWindowRunning = None
        self._create_widgets()

    def _create_widgets(self):
        self.btnAdd = ctk.CTkButton( self, text="Add", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._add)
        self.btnAdd.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.btnEdit = ctk.CTkButton( self, text="Edit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._edit)
        self.btnEdit.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.btnDel = ctk.CTkButton( self, text="Delete", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._delete)
        self.btnDel.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.btnExt = ctk.CTkButton( self, text="Exit", fg_color="blue", hover_color="gray", font=("Montserrat", 16),
                                    corner_radius=12, width=100, command=self._exit)
        self.btnExt.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

    def _add(self):
        """  Adds a friend to the friend store.
        """
        self.AddWindowRunning = saf.FriendAddWindow(self, self.friendsStore)

    def _edit(self):
        pass

    def _delete(self):
        pass

    def _exit(self):
        """  Closes the window.
        """
        self.master.destroy()

