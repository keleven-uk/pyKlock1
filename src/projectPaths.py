###############################################################################################################
#    projectPaths.py   Copyright (C) <2024>  <Kevin Scott>                                                    #
#                                                                                                             #
#    Holds common directory paths for the project.                                                            #
#        Must sit in src directory                                                                            #
#                                                                                                             #
#     For changes see history.txt                                                                             #
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

"""  A place to hold all the common project paths.
     Also, holds some common constants used in the project.
"""

import sys
import pathlib
from platformdirs import *

appname = "Klock"
appauthor = "Keleven"

USER_DATA_DIR    = pathlib.Path(user_data_dir(appname, appauthor))
USER_LOG_DIR     = pathlib.Path(user_log_dir(appname, appauthor))
USER_RUNTIME_DIR = pathlib.Path(user_runtime_dir(appname, appauthor))  #  if temp files are needed
PROJECT_PATH     = pathlib.Path(__file__).parent
MAIN_PATH        = pathlib.Path(__file__).parent.parent

print(f"USER_DATA_DIR    : {USER_DATA_DIR}")
print(f"USER_LOG_DIR     : {USER_LOG_DIR}")
print(f"USER_RUNTIME_DIR : {USER_RUNTIME_DIR}")
print(f"PROJECT_PATH     : {PROJECT_PATH}")
print(f"MAIN_PATH        : {MAIN_PATH}")

#  If running as an executable i.e. from using auto-py-to-exe.
#  Some of the paths needs to be the working directory.
#  Except the log files, these will be somewhere like C:\Users\kevin\AppData\Local\Keleven\Klock\Logs



if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    CONFIG_PATH   = USER_DATA_DIR / "config.toml"
    LOGGER_PATH   = USER_LOG_DIR / "pyKlock.log"
    HISTORY_PATH  = "History.txt"
    LICENSE_PATH  = "LICENSE.txt"
    RESOURCE_PATH = "resources"
    HELP_PATH     = "help"
else:
    CONFIG_PATH   = MAIN_PATH / "config.toml"
    LOGGER_PATH   = MAIN_PATH / "logs/pyKlock.log"
    HISTORY_PATH  = MAIN_PATH / "docs/History.txt"
    LICENSE_PATH  = MAIN_PATH / "LICENSE.txt"
    RESOURCE_PATH = MAIN_PATH / "resources"
    HELP_PATH     = MAIN_PATH / "help"

