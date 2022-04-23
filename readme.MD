# ColorfulWords
`version 1.0.0`

Package adds many functionalities related to outputting text in color, listed below. If used as a script (or through python -m), main.py will print random word in random color.  

### This package includes useful functionality:
* Printing in color - colorprinting.py module
* Logging in color - colorlogging.py module
* Generating random words - randword.py module
  * and more!

## Functions for color printing:
* **printRed** - Prints in red
* **printGreen** - Prints in green
* **printYellow** - Prints in yellow
* **printBlue** - Prints in blue
* **printPurple** - Prints in purple
* **printCyan** - Prints in cyan
* **printGray** - Prints in gray
* **printWhite** - Prints in white
* **printBlack** - Prints in black

## Color Logging functionality:
* **DEBUG** - Now in gray
* **INFO** - Now in green
* **WARNING** - Now in yellow
* **ERROR** - Now in red
* **CRITICAL** - Now in red

`Note:` Logging format, format dictionary, and handler in global scope to automatically set logging colors on import.

## Other functions contained in this module:
* **randword** - returns random word
* **colorCode** - returns ANSI code value of respective color
* **onlyLowerCaseAlpha** - returns formatted text with only lowercase, alphabetical characters
* **main** - If used as a script or with -m commands. Prints random word in random color.

`Requirements:` This package requires that packages in the requirements.txt file be installed within the Python environment you are importing this package to.

## Start Guide
### For Help
```commandline
python -m ColorfulWords -h
```

### To enable logging, import the colorlogging.py module
```doctest
import ColorfulWords.colorlogging
```
or
```doctest
from ColorfulWords import colorlogging
```

### To change log color:
```commandline
python -m ColorfulWords debug white
```
or edit the settings.json file:
```json
{
  "debug": "new color"
}
```

### Example
To utilize one of the functions listed above:
```doctest
from ColorfulWords.colorprinting import printRed

printRed("Hello world!") # In red
```