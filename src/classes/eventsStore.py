###############################################################################################################
#    eventsStore.py   Copyright (C) <2024>  <Kevin Scott>                                                     #
#    For changes see history.txt                                                                              #
#                                                                                                             #
#    A store class for the saving and manipulation of events.                                                 #
#                                                                                                             #
#    An event is a named object that consists data and a due date and/or due time.                            #
#                                                                                                             #
#    an event -  a data item of each item in Headers, defined below.                                          #
#                                                                                                             #
#    import src.classes.eventsStore as es                                                                     #
#                                                                                                             #
#    eventsStore     = es.eventsStore()                                                                       #
#                                                                                                             #
#    eventsStore.getHeaders           Retrieves the headers for display, as strings.                          #
#    eventsStore.getCategories        Retrieves the categories for display, as strings.                       #
#    eventsStore.addEvent(key, item)  Adds an event to the store.  Key = name, item = all data.               #
#    eventsStore.getEvent(rowKey)     Retrieves an event matching name.                                       #
#    eventsStore.getEvents()          Returns all events as a sorted list.                                    #
#    eventsStore.saveFriends()        Saves the event store to disc in CSV format.                            #
#                                                                                                             #
#    The class should load the CSF file on start up, if not an empty sore is created.                         #
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
import csv

import src.projectPaths as pp


class eventsStore():
    """  A class that implements a store for friends.
         The store is implemented as a dictionary - [key, item].
         The key is a string - Name.
         The item is a list  - Name, Date Due, Time, Due, Category, Notes.
    """

    def __init__(self):
        self.store = {}         #  Create the store, an empty dictionary.
        self.Headers    = ["Name", "Date Due", "Time Due", "Category", "Recurring", "Notes", "Left"]
        self.Categories = ["", "Birthday", "Anniversary", "Moto", "Holiday", "Appointment", "One Off Event", "Other"]
        self.storeName  = pp.EV_DATA_PATH

        self.loadEvents()


    @property
    def getHeaders(self):
        """  Returns a list of accepted event Headers i.e. Name, Date Due, Time Due etc.
        """
        return self.Headers

    @property
    def getCategories(self):
        """  Returns a list of accepted event Categories i.e. Birthday, Anniversary, Moto etc.
        """
        return self.Categories

    def addEvent(self, key, item):
        """   Stores event data into the store.
        """
        self.store[key] = item

    def deleteEvent(self, key):
        """   Deletes a event from the store if it exist, if not ignore.
        """
        if key in self.store:
            del self.store[key]

    @property
    def numberOfEvents(self):
        """  Returns the number of events in the store.
        """
        return len(self.store)

    def getEvent(self, key):
        """  Retrieves a single event in list format.
             If the key doesn't exist, return error massage in the Notes filed.'
        """
        try:
            return self.store[key]
        except KeyError:
            return ["", "", "", "", "", "Record not found", ""] #  May need to extend for extra fields,
                                                                 #  so the error message is always in the notes field.
    def getEvents(self):
        """  Retrieves events in list format.
        """
        lstEvent = []
        for key in sorted(self.store):
            lstEvent.append(self.store[key])

        return lstEvent

    def updateEvents(self):
        """  For each event in the store, calculate the time between the due date and now.
             The time interval, in seconds, is stored to the end of the event data,
             to be investigated later.
        """
        now = datetime.datetime.now()

        for key in self.store:
            dateDue = self.store[key][1]
            dateDue = self._checkYear(dateDue, now)
            timeDue = self.store[key][2]
            dtDue   = datetime.datetime.strptime(f"{dateDue} {timeDue}", "%d/%m/%Y %M:%H")  #  Now a dateTime
            dtLeft  = (dtDue - now).total_seconds()               #  Convert timedelta to seconds.

            if dtLeft < 61:                                       #  If dtLeft is less the a minute, flag event has due.
                self._eventDue(key)

            self.store[key][6] = self._formatSeconds(dtLeft)      #  Time left in seconds.

    def _checkYear(self, dateDue, now):
        """  Rule 1 : If the year if before the current year [i.e. original birthday year] use current year.
             Rule 2 : If the month is before the current month [i.e. original birthday month] add 1 to year.
             Rule 3 : If the day is before the current day [i.e. original birthday day] add 1 to year.

             for example - if now if 27/11/2024 and date due is 02/04/1958.
                           Should return 02/04/2025.

             Both dateDue input and output are in string format.
             now is input in datetime format.
        """
        curDay   = now.day
        curMonth = now.month
        curYear  = now.year
        dueDay   = int(dateDue[0:2])
        dueMonth = int(dateDue[3:5])
        dueYear  = int(dateDue[6:])

        if dueYear < curYear:
            dueYear = curYear
        if dueMonth < curMonth:
            dueYear = curYear + 1
        if dueDay < curDay:
            dueYear = curYear + 1

        return f"{dueDay}/{dueMonth}/{dueYear}"

    def _eventDue(self, key):
        """  Called when an event is found to be due
        """
        eventDue = self.store[key]
        print(f" Event due {eventDue}")

    def saveEvents(self):
        """  Saves the event store to a text file in csv format.
        """
        with open (self.storeName, "w", newline="", encoding="utf-8") as csvFile:
            writer =csv.writer(csvFile, quoting=csv.QUOTE_ALL)
            for key in sorted(self.store):
                writer.writerow(self.store[key])

    def loadEvents(self):
        """  Loads the event store from a text file in csv format.
        """
        try:
            with open (self.storeName, "r", encoding="utf-8") as csvFile:
                csvFile = csv.reader(csvFile)
                for rows in csvFile:
                    key = f"{rows[0]}"
                    item = rows
                    self.store[key] = item

        except FileNotFoundError:
            print("Event store not found, using empty sore.")


    def _formatSeconds(self, seconds):
        """  Formats number of seconds into a human readable form i.e. hours:minutes:seconds

            Based form klock_utils.py, to make the class self accessing.
        """
        (days, remainder)  = divmod(seconds, 86400)
        (hours, remainder) = divmod(remainder, 3600)
        (minutes, seconds) = divmod(remainder, 60)

        if days:
            return f"{days:.0f}d {hours:.0f}h:{minutes:.0f}m"
        elif hours:
            return f"{hours:.0f}h {minutes:.0f}m"
        else:
            return f"{minutes:.0f}m"






