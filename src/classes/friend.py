###############################################################################################################
#    Friend.py   Copyright (C) <2024>  <Kevin Scott>                                                          #
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

from dataclasses import dataclass

@dataclass(order=True)              #  will allow sorting later.
class Friend():
    """  A class to hold a friend.
    """
    title        : str
    surName      : str
    lastName     : str
    mobileNumber : str
    EMail        : str
    birthDay     : str
    address      : str


    def __post_init__(self):
        """  Checks if the data value is of type string, if not make see it to None.
        """
        if not isinstance(self.title, (string)):
            self.title = None
