###############################################################################################################
#    sounds.py   Copyright (C) <2024>  <Kevin Scott>                                                          #
#    For changes see history.txt                                                                              #
#                                                                                                             #
#    A class for managing sounds.                                                                             #
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
#      import src.classes.sounds as snds                                                                      #
#                                                                                                             #
#      self.sounds      = snds.Sounds(self.myConfig)                                                          #
#                                                                                                             #
#      self.sounds.playSounds()  - will play sounds depending upon options.                                   #
#                                                                                                             #
#      Current options -                                                                                      #
#                       Play chimes ever hour.                                                                #
#                       Play chimes ever quarter.                                                             #
#                       Plat the pips on the hour.                                                            #
#                                                                                                             #
#      Probably needs volume control.                                                                         #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

from audioplayer import AudioPlayer

import src.selectTime as st
import src.projectPaths as pp

class Sounds():
    """  A class for managing sounds.

         Should only be called if config setting is set to True.

         If SOUNDS_HOUR_CHIMES is called then Westminster type chimes are played on the hour.
         If SOUNDS_QUARTER_CHIMES is called then Westminster type chimes are played on the quarter hour.
         If SOUNDS_HOUR_PIPS is called then the BBC type pips are played on the hour.
    """

    def __init__(self, myConfig):
        self.myConfig = myConfig

        self.selectTime = st.SelectTime()

        self.strHour = {
            0  : "twelve",
            1  : "one",
            2  : "two",
            3  : "three",
            4  : "four",
            5  : "five",
            6  : "six",
            7  : "seven",
            8  : "eight",
            9  : "nine",
            10 : "ten",
            11 : "eleven",
            12 : "twelve"}

    def playSounds(self):
        """  Called to play the actual sounds.
             The config file should of been read in __init__.
        """

        timeText = self.selectTime.getTime("Local Time")
        hours    = int(timeText[0:2])
        minutes  = int(timeText[3:5])
        seconds  = int(timeText[6:])
        sndPath  = ""

        if seconds != 0:                        #  Only continue if seconds are zero, sounds on the hour or quarter.
            return

        if hours > 12:
            hours -= 12                         #  Work on a 12 hour klock.

        if self.myConfig.SOUNDS_HOUR_CHIMES:
            if minutes == 0:
                sndPath = f"{pp.RESOURCE_PATH}\\Sounds\\{self.strHour[hours]}.mp3"

        if self.myConfig.SOUNDS_QUARTER_CHIMES:
            if minutes in [15, 30, 45]:
                match minutes:
                    case 15:
                        sndPath = f"{pp.RESOURCE_PATH}\\Sounds\\quarterchime.mp3"
                    case 30:
                        sndPath = f"{pp.RESOURCE_PATH}\\Sounds\\halfchime.mp3"
                    case 45:
                        sndPath = f"{pp.RESOURCE_PATH}\\Sounds\\threequarterchime.mp3"

        if self.myConfig.SOUNDS_HOUR_PIPS and not self.myConfig.SOUNDS_HOUR_CHIMES:  #  If both enabled, just play hour chimes.
            if minutes == 0:
                sndPath = f"{pp.RESOURCE_PATH}\\Sounds\\thepips.mp3"

        if sndPath:
            # Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
            try:
                player = AudioPlayer(sndPath)
                player.volume = self.myConfig.SOUND_VOLUME
                player.play(block=True)
            except Exception as e:
                print(f"Error {e}")



