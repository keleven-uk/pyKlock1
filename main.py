###############################################################################################################
#    pyKlock1   Copyright (C) <2024>  <Kevin Scott>                                                           #
#                                                                                                             #
#    The Klock displays the time [local], date, key status  and the computers idle time.                      #
#       Key status is the status of Caps Lock, Scroll lock and Num lock.                                      #
#                                                                                                             #
#    For changes see history.txt                                                                              #
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

import sys
import platform

import src.config as Config
import src.logger as Logger
import src.pyKlock as Klock
import src.myTimer as Timer
import src.projectPaths as pp
import src.utils.klock_utils as utils

############################################################################################### __main__ ######


if __name__ == "__main__":
    myTimer = Timer.Timer()                                     #  Create a timer.

    message1 = utils.checkPath(pp.USER_DATA_DIR)                #  Need to check these directories exist before starting logger.
    message2 = utils.checkPath(pp.USER_LOG_DIR)

    myLogger = Logger.get_logger(str(pp.LOGGER_PATH))           # Create the logger.

    myLogger.info("-" * 100)

    try:
        myTimer.Start()                                         #  Timer mainly used to measure Klock up time.
    except (TimeoutError, AttributeError, NameError) as error:
        myLogger.debug(error)

    myConfig  = Config.Config(pp.CONFIG_PATH, myLogger)         # Create the config.

    myLogger.info(f"  Running {myConfig.NAME} Version {myConfig.VERSION} .::. Started at {myTimer.rightNow} ")
    myLogger.debug(f" {platform.uname()}")
    myLogger.debug(f" Python Version {platform.python_version()}")
    myLogger.debug("")

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        myLogger.info("  Running a frozen binary - probably via pyinstaller.")
        myLogger.info(message1)
        myLogger.info(message1)

    myLogger.info(f"  Config path   : {pp.CONFIG_PATH}")
    myLogger.info(f"  Logger path   : {pp.LOGGER_PATH}")
    myLogger.info(f"  History path  : {pp.HISTORY_PATH}")
    myLogger.info(f"  License path  : {pp.LICENSE_PATH}")
    myLogger.info(f"  Resource path : {pp.RESOURCE_PATH}")
    myLogger.info(f"  Help path     : {pp.HELP_PATH}")

    # Create an instance of the App class.
    app = Klock.Klock(myLogger, myConfig, myTimer)
    # Run the mainloop() method to start the application.
    app.mainloop()

    try:
        timeStop = myTimer.Stop
    except (TimeoutError, AttributeError, NameError) as error:
        myLogger.debug(error)
        timeStop = "00:00"

    myLogger.info(f"  Ending {myConfig.NAME} Version {myConfig.VERSION} .::. Completed in {timeStop} ")
    myLogger.info("=" * 100)
