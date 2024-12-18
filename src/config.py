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
            self.__writeDefaultConfig()
            self. logger.debug("Running program with default configure settings.")
        except toml.TomlDecodeError:
            self.logger.error("Error reading configure file.")
            self.logger.debug("Writing default configure file.")
            self.__writeDefaultConfig()
            self.logger.debug("Running program with default configure settings.")

        self.__CheckVersion()

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
    def APPEARANCE_MODE(self):
        """  Returns the application appearance mode.
             Supported modes : Light, Dark, System.
        """
        value = self.config["APPLICATION"].get("appearanceMode", "Dark")
        return value

    @APPEARANCE_MODE.setter
    def APPEARANCE_MODE(self, value):
        """  Sets the application appearance mode.
        """
        self.config["APPLICATION"]["appearanceMode"] = value

    @property
    def COLOR_THEME(self):
        """  Returns the window background colour.
             Supported themes : green, dark-blue, blue.
        """
        value = self.config["APPLICATION"].get("colorTheme", "dark-blue")
        return value

    @COLOR_THEME.setter
    def COLOR_THEME(self, value):
        """  Sets the window background colour.
        """
        self.config["APPLICATION"]["colorTheme"] = value

    @property
    def FOREGROUND(self):
        """  Returns the window foreground colour.
        """
        value = self.config["APPLICATION"].get("foreground", "#00ff00")
        return value

    @FOREGROUND.setter
    def FOREGROUND(self, value):
        """  Sets the window foreground colour.
        """
        self.config["APPLICATION"]["foreground"] = value

    @property
    def BACKGROUND(self):
        """  Returns the window background colour.
        """
        value = self.config["APPLICATION"].get("background", "000000")
        return value

    @BACKGROUND.setter
    def BACKGROUND(self, value):
        """  Sets the window background colour.
        """
        self.config["APPLICATION"]["background"] = value

    @property
    def TRANSPARENT(self):
        """  Returns the window transparent.
        """
        return self.config["APPLICATION"].get("transparent", True)

    @TRANSPARENT.setter
    def TRANSPARENT(self, value):
        """  Sets the window transparent.
        """
        self.config["APPLICATION"]["transparent"] = value

    @property
    def WIN_WIDTH(self):
        """  Returns the window width.
        """
        return self.config["APPLICATION"].get("width", "400")

    @WIN_WIDTH.setter
    def WIN_WIDTH(self, value):
        """  Sets the window width.
        """
        self.config["APPLICATION"]["width"] = value

    @property
    def WIN_HEIGHT(self):
        """  Returns the window height.
        """
        return self.config["APPLICATION"].get("height", "150")

    @WIN_HEIGHT.setter
    def WIN_HEIGHT(self, value):
        """  Sets the window height.
        """
        self.config["APPLICATION"]["height"] = value

    @property
    def X_POS(self):
        """  Returns the X co-ordinate of the top right hand corner of the window.
        """
        return self.config["APPLICATION"].get("x_pos", "0")

    @X_POS.setter
    def X_POS(self, value):
        """  Sets the X co-ordinate of the top right hand corner of the window.
        """
        self.config["APPLICATION"]["x_pos"] = value

    @property
    def Y_POS(self):
        """  Returns the Y co-ordinate of the top right hand corner of the window.
        """
        return self.config["APPLICATION"].get("y_pos", "0")

    @Y_POS.setter
    def Y_POS(self, value):
        """  Sets the Y co-ordinate of the top right hand corner of the window.
        """
        self.config["APPLICATION"]["y_pos"] = value

    @property
    def ALIGN_RIGHT(self):
        """  Returns the Y co-ordinate of the top right hand corner of the window.
        """
        return self.config["APPLICATION"].get("Align_Right", True)

    @ALIGN_RIGHT.setter
    def ALIGN_RIGHT(self, value):
        """  Sets the Y co-ordinate of the top right hand corner of the window.
        """
        self.config["APPLICATION"]["Align_Right"] = value

    @property
    def TIME_TYPE(self):
        """  Return the type [format] of the displayed time.
        """
        return self.config["TIME"].get("type", "GMT Time")

    @TIME_TYPE.setter
    def TIME_TYPE(self, value):
        """  Sets if menu visible.
        """
        self.config["TIME"]["type"] = value

    @property
    def MENU_VISIBLE(self):
        """  Return the if menu visible.
        """
        return self.config["MENU"].get("visible", True)

    #  Time Font config options.
    @property
    def TIME_FONT_FAMILY(self):
        """  Return the main time display family.
        """
        return self.config["TIME_FONT"].get("family", "Pendule Ornamental")

    @TIME_FONT_FAMILY.setter
    def TIME_FONT_FAMILY(self, value):
        """  Sets the main time display family.
        """
        self.config["TIME_FONT"]["family"] = value

    @property
    def TIME_FONT_SIZE(self):
        """  Return the main time display font size.
        """
        return self.config["TIME_FONT"].get("size", 100)

    @TIME_FONT_SIZE.setter
    def TIME_FONT_SIZE(self, value):
        """  Sets the main time display font size.
        """
        self.config["TIME_FONT"]["size"] = value

    #  Status bar font config options.
    @property
    def STATUS_FONT_FAMILY(self):
        """  Return the status bar font family.
        """
        return self.config["STATUS_FONT"].get("family", "default")

    @STATUS_FONT_FAMILY.setter
    def STATUS_FONT_FAMILY(self, value):
        """  Sets the status bar font family.
        """
        self.config["STATUS_FONT"]["family"] = value

    @property
    def STATUS_FONT_SIZE(self):
        """  Return the status bar font size.
        """
        return self.config["STATUS_FONT"].get("size", 12)

    @STATUS_FONT_SIZE.setter
    def STATUS_FONT_SIZE(self, value):
        """  Sets the status bar font size.
        """
        self.config["STATUS_FONT"]["size"] = value

    #  VFD Klock config options.
    @property
    def VFD_WIDTH(self):
        """  Returns the vfdKlock width.
        """
        return self.config["KLOCKS"].get("vfd_width", "500")

    @VFD_WIDTH.setter
    def VFD_WIDTH(self, value):
        """  Sets the vfdKlock width.
        """
        self.config["KLOCKS"]["vfd_width"] = value

    @property
    def VFD_HEIGHT(self):
        """  Returns the vfdKlock height.
        """
        return self.config["KLOCKS"].get("vfd_height", "260")

    @VFD_HEIGHT.setter
    def VFD_HEIGHT(self, value):
        """  Sets the vfdKlock height.
        """
        self.config["KLOCKS"]["vfd_height"] = value

    @property
    def VFD_X_POS(self):
        """  Returns the vfdKlock x pos.
        """
        return self.config["KLOCKS"].get("vfd_x_pos", "400")

    @VFD_X_POS.setter
    def VFD_X_POS(self, value):
        """  Sets the vfdKlock x pos.
        """
        self.config["KLOCKS"]["vfd_x_pos"] = value

    @property
    def VFD_Y_POS(self):
        """  Returns the vfdKlock y pos.
        """
        return self.config["KLOCKS"].get("vfd_y_pos", "400")

    @VFD_Y_POS.setter
    def VFD_Y_POS(self, value):
        """  Sets the vfdKlock y pos.
        """
        self.config["KLOCKS"]["vfd_y_pos"] = value

    @property
    def VFD_FOREGROUND(self):
        """  Returns the vfdKlock foreground colour.
        """
        return self.config["KLOCKS"].get("vfd_foreground", "#82ccff")

    @VFD_FOREGROUND.setter
    def VFD_FOREGROUND(self, value):
        """  Sets the vfdKlock foreground colour.
        """
        self.config["KLOCKS"]["vfd_foreground"] = value

    @property
    def VFD_BACKGROUND(self):
        """  Returns the vfdKlock background colour.
        """
        return self.config["KLOCKS"].get("vfd_background", "#000000")

    @VFD_BACKGROUND.setter
    def VFD_BACKGROUND(self, value):
        """  Sets the vfdKlock background colour.
        """
        self.config["KLOCKS"]["vfd_background"] = value

    #  Text Klock config options.
    @property
    def TEXTKLOCK_WIDTH(self):
        """  Returns the textKlock width.
        """
        return self.config["KLOCKS"].get("textKlock_width", "460")

    @TEXTKLOCK_WIDTH.setter
    def TEXTKLOCK_WIDTH(self, value):
        """  Sets the textKlock width.
        """
        self.config["KLOCKS"]["textKlock_width"] = value

    @property
    def TEXTKLOCK_HEIGHT(self):
        """  Returns the textKlock height.
        """
        return self.config["KLOCKS"].get("textKlock_height", "260")

    @TEXTKLOCK_HEIGHT.setter
    def TEXTKLOCK_HEIGHT(self, value):
        """  Sets the textKlock height.
        """
        self.config["KLOCKS"]["textKlock_height"] = value

    @property
    def TEXTKLOCK_X_POS(self):
        """  Returns the textKlock x pos.
        """
        return self.config["KLOCKS"].get("textKlock_x_pos", "400")

    @TEXTKLOCK_X_POS.setter
    def TEXTKLOCK_X_POS(self, value):
        """  Sets the textKlock x pos.
        """
        self.config["KLOCKS"]["textKlock_x_pos"] = value

    @property
    def TEXTKLOCK_Y_POS(self):
        """  Returns the textKlock y pos.
        """
        return self.config["KLOCKS"].get("textKlock_y_pos", "400")

    @TEXTKLOCK_Y_POS.setter
    def TEXTKLOCK_Y_POS(self, value):
        """  Sets the textKlock y pos.
        """
        self.config["KLOCKS"]["textKlock_y_pos"] = value

    @property
    def TEXTKLOCK_ON_COLOUR(self):
        """  Returns the textdKlock on colour.
        """
        return self.config["KLOCKS"].get("textKlock_onColour", "springGreen2")

    @TEXTKLOCK_ON_COLOUR.setter
    def TEXTKLOCK_ON_COLOUR(self, value):
        """  Sets the textKlock on colour.
        """
        self.config["KLOCKS"]["textKlock_onColour"] = value

    @property
    def TEXTKLOCK_OFF_COLOUR(self):
        """  Returns the textdKlock off colour.
        """
        return self.config["KLOCKS"].get("textKlock_offColour", "slate grey")

    @TEXTKLOCK_OFF_COLOUR.setter
    def TEXTKLOCK_OFF_COLOUR(self, value):
        """  Sets the textKlock off colour.
        """
        self.config["KLOCKS"]["textKlock_offColour"] = value

    @property
    def TEXTKLOCK_BACKGROUND(self):
        """  Returns the textKlock background colour.
        """
        return self.config["KLOCKS"].get("textKlock_background", "#000000")

    @TEXTKLOCK_BACKGROUND.setter
    def TEXTKLOCK_BACKGROUND(self, value):
        """  Sets the textKlock background colour.
        """
        self.config["KLOCKS"]["textKlock_background"] = value

    @property
    def SOUNDS(self):
        """  Returns if sounds are enabled.
        """
        return self.config["SOUNDS"].get("sounds", True)

    @SOUNDS.setter
    def SOUNDS(self, value):
        """  Sets if sounds are enabled.
        """
        self.config["SOUNDS"]["sounds"] = value

    @property
    def SOUNDS_HOUR_CHIMES(self):
        """  Returns if hour chimes are enabled.
        """
        return self.config["SOUNDS"].get("hour_chimes", True)

    @SOUNDS_HOUR_CHIMES.setter
    def SOUNDS_HOUR_CHIMES(self, value):
        """  Sets if hour chimes are enabled.
        """
        self.config["SOUNDS"]["hour_chimes"] = value

    @property
    def SOUNDS_QUARTER_CHIMES(self):
        """  Returns if quarter chimes are enabled.
        """
        return self.config["SOUNDS"].get("quarter_chimes", True)

    @SOUNDS_QUARTER_CHIMES.setter
    def SOUNDS_QUARTER_CHIMES(self, value):
        """  Sets if quarter chimes are enabled.
        """
        self.config["SOUNDS"]["quarter_chimes"] = value

    @property
    def SOUNDS_HOUR_PIPS(self):
        """  Returns if hour pips are enabled.
        """
        return self.config["SOUNDS"].get("hour_pips", True)

    @SOUNDS_HOUR_PIPS.setter
    def SOUNDS_HOUR_PIPS(self, value):
        """  Sets if hour pips are enabled.
        """
        self.config["SOUNDS"]["hour_pips"] = value

    @property
    def SOUND_VOLUME(self):
        """  Returns if sound volume.
        """
        return self.config["SOUNDS"].get("sound_volume", True)

    @SOUND_VOLUME.setter
    def SOUND_VOLUME(self, value):
        """  Sets sound volume.
        """
        self.config["SOUNDS"]["sound_volume"] = value


    #  ------------------------------------------------------------------------------------------------------------------------

    def __CheckVersion(self):
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

                    if "SOUNDS" not in self.config:
                        #  New config options to be added at 2024.47 - Sounds
                        self.logger.info("  ** New options for Sounds added @ 2024.47**")
                        self.config["SOUNDS"] = {"hour_chimes"   : True,
                                                 "quarter_chimes": True,
                                                 "hour_pips"     : True,
                                                 "sound_volume"  : 25}

                    if self.config["KLOCKS"].get("textKlock_width" ) is None:
                        #  New config options to be added at 2024.42 - text klock
                        self.logger.info("  ** New options for TEXT Klock added @ 2024.42**")
                        self.config["KLOCKS"] = {"textKlock_width"      : 500,
                                                 "textKlock_height"     : 260,
                                                 "textKlock_x_pos"      : 821,
                                                 "textKlock_y_pos"      : 280,
                                                 "textKlock_onColour"   : "springGreen2",
                                                 "text_ofColour"        : "grey",
                                                 "textKlock_background" : "#000000"}

                    if self.config["KLOCKS"].get("vfd_width" ) is None:
                        #  New config options to be added at 2024.23 - VFD Klock
                        self.logger.info("  ** New options for VFD Klock added @ 2024.23**")
                        self.config["KLOCKS"] = {"vfd_width"      : 500,
                                                 "vfd_height"     : 260,
                                                 "vfd_x_pos"      : 400,
                                                 "vfd_y_pos"      : 400,
                                                 "vfd_foreground" : "#82ccff",
                                                 "vfd_background" : "#000000"}

                    if "APPLICATION" not in self.config:
                        #  New config options to be added at 2024.25
                        #  This is a combination of the old COLOUR and WINDOW options.
                        #  Options set to default.
                        self.logger.info("  ** New options for 2024.25 **")
                        self.config["APPLICATION"] = {"appearanceMode" : "Dark",
                                                      "colorTheme"     : "dark-blue",
                                                      "foreground"     : "#00ff00",
                                                      "background"     : "#000000",
                                                      "transparent"    : True,
                                                      "width"          : 300,
                                                      "height"         : 160,
                                                      "x_pos"          : 100,
                                                      "y_pos"          : 100,
                                                      "Align_Right"    : True}

                    #  Remove depreciated option keys
                    if "COLOUR" in self.config:
                        self.logger.info("  ** Delete depreciated option key 2024.25 **")
                        try:
                            del self.config["COLOUR"]
                        except KeyError:
                            self.logger.debug("  Problem with config key COLOUR")

                    if "WINDOW" in self.config:
                        self.logger.info("  ** Delete depreciated option key 2024.25 **")
                        try:
                            del self.config["WINDOW"]
                        except KeyError:
                            self.logger.debug("  Problem with config key WINDOW")

                    self.writeConfig()
        except FileNotFoundError:
            self.logger.error("  Version file not found.")
        except toml.TomlDecodeError:
            self.logger.error("  Error reading Version file.")

    #  ------------------------------------------------------------------------------------------------------------------------

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


    def __writeDefaultConfig(self):
        """ Write a default configure file.
            This is hard coded  ** TO KEEP UPDATED **
        """
        self.logger.info("  Writing default config.")
        strNow  = datetime.datetime.now()
        written = strNow.strftime("%A %d %B %Y  %H:%M:%S")
        config  = dict()

        config["INFO"] = {"myVERSION": "2024.47",
                          "myNAME"   : "pyKlock"}

        config["APPLICATION"] = {"appearanceMode" : "Dark",
                                 "colorTheme"     : "dark-blue",
                                 "foreground"     : "#00ff00",
                                 "background"     : "#000000",
                                 "transparent"    : True,
                                 "width"          : 300,
                                 "height"         : 160,
                                 "x_pos"          : 100,
                                 "y_pos"          : 100,
                                 "Align_Right"    : True}

        config["TIME"] = {"type": "GMT Time"}

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

        config["KLOCKS"] = {"vfd_width"       : 460,
                            "vfd_height"      : 260,
                            "vfd_x_pos"       : 400,
                            "vfd_y_pos"       : 400,
                            "vfd_foreground"  : "#82ccff",
                            "vfd_background"  : "#000000",
                            "textKlock_width"      : 500,
                            "textKlock_height"     : 260,
                            "textKlock_x_pos"      : 821,
                            "textKlock_y_pos"      : 280,
                            "textKlock_onColour"   : "springGreen2",
                            "text_ofColour"   : "slate grey",
                            "textKlock_background" : "#000000"}

        config["SOUNDS"] = {"hour_chimes"   : True,
                            "quarter_chimes": True,
                            "hour_pips"     : True,
                            "sound_volume"  : 25}


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
