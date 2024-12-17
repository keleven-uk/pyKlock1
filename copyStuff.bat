@rem  Simple script to copy the required files needed for Klock to run.
@rem
@rem   September 2024               <2024> (c) Kevin Scott

@echo OFF

copy LICENSE.txt output\Klock\
copy README.md output\Klock\
copy klock.iss output\Klock
copy docs\history.txt output\Klock\
copy docs\version.toml output\Klock

mkdir output\klock\help
copy help\klock.pdf output\Klock\help
copy help\klock.chm output\Klock\help

mkdir output\klock\resources
copy resources\tea.ico output\Klock\resources

mkdir output\klock\resources\Sounds
xcopy resources\Sounds output\Klock\resources\Sounds




