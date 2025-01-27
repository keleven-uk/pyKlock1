@rem  Simple script to copy the required files needed for pyKlock to run.
@rem
@rem   September 2024               <2024> (c) Kevin Scott

@echo OFF

copy LICENSE.txt output\pyKlock\
copy README.md output\pyKlock\
copy klock.iss output\pyKlock
copy docs\history.txt output\pyKlock\
copy docs\version.toml output\pyKlock

mkdir output\pyKlock\help
copy help\pyKlock.pdf output\pyKlock\help
copy help\pyKlock.chm output\pyKlock\help

robocopy resources output\pyKlock\resources /s /e


