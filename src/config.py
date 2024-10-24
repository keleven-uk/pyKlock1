###############################################################################################################
#    myConfig.py    Copyright (C) <2024>  <Kevin Scott>                                                       #
#                                                                                                             #
#    A class that acts has a wrapper around the configure file - config.toml.                                 #
#    The configure file is first read, then the properties are made available.                                #
#    The configure file is currently in toml format.                                                          #
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

import toml


class Config():
    """  A class that acts has a wrapper around the configure file - config.toml.
         The configure file is hard coded and lives in the same directory has the main script.
         The configure file is first read, then the properties are made available.

         If config.toml is not found, a default configure file is generated.

         The get read the directory and if the key is not found a default is returned.

         usage:
            myConfig = myConfig.Config()
    """

    def __init__(self, CONFIG_PATH, VERSION_PATH, logger):

        self.FILE_NAME = CONFIG_PATH
        self.VERS_NAME = VERSION_PATH
        self.logger    = logger

        try:
            with open(self.FILE_NAME, "r") as configFile:       # In context manager.
                self.config = toml.load(configFile)             # Load the configure file, in toml.
        except FileNotFoundError:
            self.logger.error("Configure file not found.")
            self.logger.debug("Writing default configure file.")
            self._writeDefaultConfig()
            self. logger.debug("Running program with default configure settings.")
        except toml.TomlDecodeError:
            self.logger.error("Error reading configure file.")
            self.logger.debug("Writing default configure file.")
            self._writeDefaultConfig()
            self.logger.debug("Running program with default configure settings.")

        self._CheckVersion()

    @property
    def NAME(self):
        """  Returns the application name.
        """
        return self.config["INFO"].get("myNAME", "pyDigitalKlock")

    @property
    def VERSION(self):
        """  Returns the application Version.
        """
        return self.config["INFO"]["myVERSION"]

    @property
    def FOREGROUND(self):
        """  Returns the window foreground colour.
        """
        value = self.config["COLOUR"].get("foreground", "#00ff00")
        #print(f"getting foreground to {value}")
        return value

    @FOREGROUND.setter
    def FOREGROUND(self, value):
        """  Sets the window foreground colour.
        """
        #print(f"setting foreground to {value}")
        self.config["COLOUR"]["foreground"] = value

    @property
    def BACKGROUND(self):
        """  Returns the window background colour.
        """
        value = self.config["COLOUR"].get("background", "000000")
        #print(f"getting background to {value}")
        return value

    @BACKGROUND.setter
    def BACKGROUND(self, value):
        """  Sets the window background colour.
        """
        #print(f"setting background to {value}")
        self.config["COLOUR"]["background"] = value

    @property
    def TRANSPARENT(self):
        """  Returns the window transparent.
        """
        return self.config["COLOUR"].get("transparent", True)

    @TRANSPARENT.setter
    def TRANSPARENT(self, value):
        """  Sets the window transparent.
        """
        self.config["COLOUR"]["transparent"] = value

    @property
    def WIN_WIDTH(self):
        """  Returns the window width.
        """
        return self.config["WINDOW"].get("width", "400")

    @WIN_WIDTH.setter
    def WIN_WIDTH(self, value):
        """  Sets the window width.
        """
        self.config["WINDOW"]["width"] = value

    @property
    def WIN_HEIGHT(self):
        """  Returns the window height.
        """
        return self.config["WINDOW"].get("height", "150")

    @WIN_HEIGHT.setter
    def WIN_HEIGHT(self, value):
        """  Sets the window height.
        """
        self.config["WINDOW"]["height"] = value

    @property
    def X_POS(self):
        """  Returns the X co-ordinate of the top right hand corner of the window.
        """
        return self.config["WINDOW"].get("x_pos", "0")

    @X_POS.setter
    def X_POS(self, value):
        """  Sets the X co-ordinate of the top right hand corner of the window.
        """
        self.config["WINDOW"]["x_pos"] = value

    @property
    def Y_POS(self):
        """  Returns the Y co-ordinate of the top right hand corner of the window.
        """
        return self.config["WINDOW"].get("y_pos", "0")

    @Y_POS.setter
    def Y_POS(self, value):
        """  Sets the Y co-ordinate of the top right hand corner of the window.
        """
        self.config["WINDOW"]["y_pos"] = value

    @property
    def ALIGN_RIGHT(self):
        """  Returns the Y co-ordinate of the top right hand corner of the window.
        """
        return self.config["WINDOW"].get("Align_Right", True)

    @ALIGN_RIGHT.setter
    def ALIGN_RIGHT(self, value):
        """  Sets the Y co-ordinate of the top right hand corner of the window.
        """
        self.config["WINDOW"]["Align_Right"] = value

    @property
    def TIME_TYPE(self):
        """  Return the type [format] of the displayed time.
        """
        return self.config["TIME"].get("type", "Fuzzy Time")

    @TIME_TYPE.setter
    def TIME_TYPE(self, value):
        """  Sets the type [format] of the displayed time.
        """
        self.config["TIME"]["type"] = value

    @property
    def MENU_VISIBLE(self):
        """  Return the type [format] of the displayed time.
        """
        return self.config["MENU"].get("visible", True)

    @property
    def TIME_FONT_FAMILY(self):
        """  Return the type [format] of the displayed time.
        """
        return self.config["TIME_FONT"].get("family", "Pendule Ornamental")

    @TIME_FONT_FAMILY.setter
    def TIME_FONT_FAMILY(self, value):
        """  Sets the type [format] of the displayed time.
        """
        self.config["TIME_FONT"]["family"] = value

    @property
    def TIME_FONT_SIZE(self):
        """  Return the type [format] of the displayed time.
        """
        return self.config["TIME_FONT"].get("size", 100)

    @TIME_FONT_SIZE.setter
    def TIME_FONT_SIZE(self, value):
        """  Sets the type [format] of the displayed time.
        """
        self.config["TIME_FONT"]["size"] = value

    @property
    def STATUS_FONT_FAMILY(self):
        """  Return the type [format] of the displayed time.
        """
        return self.config["STATUS_FONT"].get("family", "default")

    @STATUS_FONT_FAMILY.setter
    def STATUS_FONT_FAMILY(self, value):
        """  Sets the type [format] of the displayed time.
        """
        self.config["STATUS_FONT"]["family"] = value

    @property
    def STATUS_FONT_SIZE(self):
        """  Return the type [format] of the displayed time.
        """
        return self.config["STATUS_FONT"].get("size", 12)

    @STATUS_FONT_SIZE.setter
    def STATUS_FONT_SIZE(self, value):
        """  Sets the type [format] of the displayed time.
        """
        self.config["STATUS_FONT"]["size"] = value


    def _CheckVersion(self):
        """  Checks Klocks version against a version file - if they diff, an upgrade has been performed.
             So, amend klock's version [this save uninstalling klock to get the same result.].

             Could be used to add new config options, if needed.
        """
        try:
            with open(self.VERS_NAME, "r") as versionFile:       # In context manager.
                vers = toml.load(versionFile)             # Load the configure file, in toml.
                newVersion = vers["INFO"]["newVersion"]
                oldVersion = self.VERSION
                if newVersion != oldVersion:
                    self.config["INFO"]["myVERSION"] = newVersion
                    self.logger.info(f"  ** Klock has been upgraded from version {oldVersion} to new version {newVersion} **")
                    self.writeConfig()
        except FileNotFoundError:
            self.logger.error("  Version file not found.")
        except toml.TomlDecodeError:
            self.logger.error("  Error reading Version file.")

    def writeConfig(self):
        """ Write the current config file.
        """
        self.logger.info("  Writing current config.")
        strNow  = datetime.datetime.now()
        written = strNow.strftime("%A %d %B %Y  %H:%M:%S")
        st_toml = toml.dumps(self.config)

        with open(self.FILE_NAME, "w") as configFile:       # In context manager.
            configFile.write("#   Configure file for pyKlock.py \n")
            configFile.write(f"#   (c) Kevin Scott   Written {written}\n")
            configFile.write("#\n")
            configFile.write("#   true and false are lower case \n")
            configFile.write("#\n")

            configFile.writelines(st_toml)


    def _writeDefaultConfig(self):
        """ Write a default configure file.
            This is hard coded  ** TO KEEP UPDATED **
        """
        self.logger.info("  Writing default config.")
        strNow  = datetime.datetime.now()
        written = strNow.strftime("%A %d %B %Y  %H:%M:%S")
        config  = dict()

        config["INFO"] = {"myVERSION": "2024.22",
                          "myNAME"   : "pyKlock"}

        config["COLOUR"] = {"foreground" : "#00ff00",
                            "background" : "#000000",
                            "transparent": True}

        config["WINDOW"] = {"width"        :300,
                            "height"       :160,
                            "x_pos"        :100,
                            "y_pos"        :100,
                             "Align_Right" : True}

        config["TIME"] = {"type": "Fuzzy Time"}

        config["MENU"] = {"visible": True}

        config["TIME_FONT"] = {"family"     : "Pendule Ornamental",
                               "size"       : 100,
                               "weight"     : "normal",
                               "slant"      : False,
                               "underline"  : False,
                               "overstrike" : False}

        config["STATUS_FONT"] = {"family"   : "Default",
                               "size"       : 12,
                               "weight"     : "normal",
                               "slant"      : False,
                               "underline"  : False,
                               "overstrike" : False}


        st_toml = toml.dumps(config)

        with open(self.FILE_NAME, "w") as configFile:       # In context manager.
            configFile.write("#   DEFAULT Configure file for pyKlock.py \n")
            configFile.write(f"#   (c) Kevin Scott   Written {written}\n")
            configFile.write("#\n")
            configFile.write("#   true and false are lower case \n")
            configFile.write("\n")
            configFile.writelines(st_toml)                  # Write configure file.

        with open(self.FILE_NAME, "r") as configFile:       # In context manager.
            self.config = toml.load(configFile)             # Load the configure file, in toml.
