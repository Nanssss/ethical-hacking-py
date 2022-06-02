#!/bin/bash

rm -r dist/
rm -r build/
rm *.spec
wine /home/kamui/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile $1
