@rem  Simple script to copy the required files needed for pyKlock to run.
@rem
@rem   September 2024               <2024> (c) Kevin Scott

@echo OFF

copy LICENSE.txt output\pyKlock\
copy README.md output\pyKlock\
copy klock.iss output\pyKlock
copy docs\history.txt output\pyKlock\
copy docs\version.toml output\pyKlock

mkdir output\klock\help
copy help\klock.pdf output\pyKlock\help
copy help\klock.chm output\pyKlock\help

mkdir output\klock\resources
copy resources\tea.ico output\pyKlock\resources

mkdir output\klock\resources\Sounds
xcopy resources\Sounds output\pyKlock\resources\Sounds




