from cx_Freeze import setup, Executable
import tkinter
import sys, os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base='Win32GUI'

executables = [Executable("GUI.py", base=base)]

packages = ["idna"]

options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name = "Resistor Calculate",
    options = options,
    version = 1.0,
    description = "Calculation of the various bands of resistors and chip resistors",
    executables = executables
)

