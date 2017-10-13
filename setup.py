import sys
from cx_Freeze import setup, Executable
import os.path

includefiles = ['sound/', 'images/']

# Fixes dependency issue with pygame rendering
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pygame"], "excludes": ["tkinter"], 'include_files':includefiles, "optimize": 1}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Trump Invaders",
		version = "0.1",
		description = "Trump Invaders",
		options = {"build_exe": build_exe_options},
		executables = [Executable(
			"alien_invasion.py",
			base=base,
		)]
)