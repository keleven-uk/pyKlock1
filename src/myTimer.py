###############################################################################################################
#    myTimer.py   Copyright (C) <2020-2024>  <Kevin Scott>                                                    #
#                                                                                                             #
#    Inspired by https://realpython.com/python-timer/                                                         #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2020-2024>  <Kevin Scott>                                                                 #
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

import time
import datetime as dt


class TimerError(Exception):
    """  A custom exception used to report errors in use of Timer class.
    """

class Timer():
    """  A simple timer.

        t.Start     - will start the timer.
        t.Elapsed   - will return the elapsed time since the time started.
        t.Stop      - will return the time since the time started and stop the timer.
        t.rightNow  - will Returns the current date and time in the format HH:MM:SS, DD/MM/YYYY.

        The methods have been converted to property's, makes the syntax cleaner.
        The methods above Will raise an exception is there is an error.

        t.formatSeconds - Formats number of seconds into a human readable form i.e. hours:minutes:seconds
                          Method made available so it can be used within and outside of class.

    """
    def __init__(self):
        self.__start_time = None

    def Start(self):
        """  Start a new timer.

             app - True indicates time the executable time of an App.
        """
        if self.__start_time is not None:
            raise TimerError("Timer is running. Use .stop to stop it")

        self.__start_time = time.perf_counter()

    @property
    def Elapsed(self):
        """  Return the elapsed time since start, but does not stop the timer.
        """
        if self.__start_time is None:
            raise TimerError("Timer is not running. Use .start to start it")

        __elapsed_time = time.perf_counter() - self.__start_time
        return self.formatSeconds(__elapsed_time)

    @property
    def Stop(self):
        """  Stop the timer, and report the elapsed time.
        """
        if self.__start_time is None:
            raise TimerError("Timer is not running. Use .start to start it")

        __elapsed_time = time.perf_counter() - self.__start_time
        self.__start_time = None
        return self.formatSeconds(__elapsed_time)

    @property
    def rightNow(self):
        """  Returns the current date and time in the format HH:MM:SS, DD/MM/YYYY.
        """
        mtime = dt.datetime.now()
        return mtime.strftime("%H:%M:%S : %d/%m/%Y")

    def formatSeconds(self, seconds):
        """  Formats number of seconds into a human readable form i.e. hours:minutes:seconds

             Method made available so it can be used within and outside of class.
        """
        minutes, seconds = divmod(seconds, 60)
        hours, minutes   = divmod(minutes, 60)

        if hours:
            return f"{hours}h:{minutes}m:{seconds:0.0f}s"
        elif minutes:
            return f"{minutes}m:{seconds:0.0f}s"
        else:
            return f"{seconds:0.0f}s"
