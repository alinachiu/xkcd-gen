# RandomPasswordGenerator
A random password generator written in Python3 which generates passwords using the [xkcd](https://xkcd.com/936/) password generating method. Uses a text file filled with over 466k English words as well as a combination of symbols and numbers to generate strong passwords. The program can be run as a Unix executable file (xkcdpwgen with no extension), but the source code is provided as xkcdpwgen.py as well.

## Terminal Commands
The user can tell the program how many words, capitals, numbers, and symbols they want to have in their randomly generated password. If they ever get stuck, -h or --help can be used to display a help message with all of the commands.
Can run in terminal using the following command (items in [] are addtional commands): xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]
- -h, --help: show this help message and exit
- -w WORDS, --words WORDS: include WORDS words in the password (default=4)
- -c CAPS, --caps CAPS: capitalize the first letter of CAPS random words (default=0)
- -n NUMBERS, --numbers NUMBERS: insert NUMBERS random numbers in the password (default=0)
- -s SYMBOLS, --symbols SYMBOLS: insert SYMBOLS random symbols in the password (default=0)
