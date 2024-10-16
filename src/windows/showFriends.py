###############################################################################################################
#    SelectFriends.py   Copyright (C) <2024>  <Kevin Scott>                                                   #
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
import CTkTable as ctkTable

import src.CTkXYFrame as CTkXY
import src.windows.showAddFriend as saf

import src.classes.friend as friend

class FriendsWindow(ctk.CTkToplevel):
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
        self.resizable(False, False)

        self._create_widgets()


    def _create_widgets(self):
        """  Create the main time display.
        """
        self.tf = topFrame(self, self.myConfig)
        self.tf.pack(fill="both", expand=True)
        self.bf = ButtonFrame(self, self.myConfig)
        self.bf.pack(padx=10, pady=10)


class topFrame(CTkXY.CTkXYFrame):
    """  A class for the top form of the about window.
         The display general information about Klock.
    """
    def __init__(self, master, myConfig):
        super().__init__(master)

        self._create_widgets()

    def _create_widgets(self):

        value = [["No", "Title","Surname","Last Name","Mobile No","E Mail","Birth Day", "Address"],
                ["1", "Ms","Sue","Cleret-Scott","07874 713219", "sue@seleven.co.uk", "11 October 1960", "22 Laburnam Walk, Gilberdyke, HU15 2TU"],
                ["2", "Mr","Kevin","Scott","07742 589160", "kevin@keleven.co.uk", "2 April 1958", "22 Laburnam Walk, Gilberdyke, HU15 2TU"],
                ["3", 1,2,3,4,5,5,88],
                ["4", 1,2,3,4,5],
                ["5", 1,2,3,4,5,8,12],
                ["6", 1,2,3,4,5,8,12],
                ["7", 1,2,3,4,5,8,12],
                ["8", 1,2,3,4,5,8,12],
                ["9", "Title","Surname","Last Name","Mobile No","E Mail","Birth Day", "Address"],
                ["10", 1,2,3,4,5,8,12],
                ["11", "Title","Surname","Last Name","Mobile No","E Mail","Birth Day", "Address"],
                ["12", "Title","Surname","Last Name","Mobile No","E Mail","Birth Day", "Address"]]

        tblFriends = ctkTable.CTkTable(self, column=8, width=100, values=value, hover=True, command=self.pressed)
        tblFriends.pack(expand=True)


    def pressed(self, block):
        print(block)


class ButtonFrame(ctk.CTkFrame):
    """  A class for the top form of the about window.
         The display general information about Klock.
    """
    def __init__(self, master, myConfig, **kwargs):
        super().__init__(master, **kwargs)

        self.myConfig = myConfig

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
        newFriend = saf.FriendAddWindow(self, self.myConfig)


    def _edit(self):
        pass

    def _delete(self):
        pass

    def _exit(self):
        """  Closes the window.
        """
        self.master.destroy()

