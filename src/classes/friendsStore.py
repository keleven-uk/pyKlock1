###############################################################################################################
#    friendsStore.py   Copyright (C) <2024>  <Kevin Scott>                                                    #
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

import csv

import src.projectPaths as pp


class friendsStore():
    """  A class that implements a store for friends.
         The store is implemented as a dictionary - [key, item].
         The key is a string - Last Name : First Name.
         The item is a list  - Title, First Name, Last Name, Mobile No, Email, Birthday.
    """

    def __init__(self):
        self.store     = {}         #  Create the store, an empty dictionary.
        self.titles    = ["", "Mr", "Ms", "Mrs", "Miss", "Dr"]
        self.Headers   = ["Title", "First name", "Last name", "Mobile Number", "Telephone Number", "eMail", "Birthday",
                          "House Number", "Address Line 1","Address Line 2", "City", "County", "Post Code", "Country"]
        self.storeName = pp.FR_DATA_PATH

        self.loadFriends()

    @property
    def getTitles(self):
        """  Returns a list of accepted friend titles i.e. mr and mrs etc.
        """
        return self.titles

    @property
    def getHeaders(self):
        """  Returns a list of accepted friend Headers i.e. mr and mrs etc.
        """
        return self.Headers

    def addFriend(self, key, item):
        """   Stores friend data into the store.
        """
        self.store[key] = item

    def deleteFriend(self, key):
        """   Deletes a friend from the store if it exist, if not ignore.
        """
        if key in self.store:
            del self.store[key]

    @property
    def numberOfFriends(self):
        """  Returns the number of friends in the store.
        """
        return len(self.store)

    def getFriend(self, key):
        """  Retrieves a single friend in list format.
        """
        return self.store[key]

    def getFriends(self):
        """  Retrieves friends in list format.
        """
        lstFriends = []
        for key in sorted(self.store):
            lstFriends.append(self.store[key])

        return lstFriends

    def saveFriends(self):
        """  Saves the friend store to a text file in csv format.
        """
        with open (self.storeName, "w", newline="") as csvFile:
            writer =csv.writer(csvFile, quoting=csv.QUOTE_ALL)
            for key in sorted(self.store):
                writer.writerow(self.store[key])

    def loadFriends(self):
        """  Loads the friend store from a text file in csv format.
        """
        try:
            with open (self.storeName, "r") as csvFile:
                csvFile = csv.reader(csvFile)
                for rows in csvFile:
                    key = f"{rows[1]} : {rows[2]}"
                    item = rows
                    self.store[key] = item

        except FileNotFoundError:
            print("File not found, will use an empty store.")
