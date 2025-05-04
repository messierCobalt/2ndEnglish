import os, sys, time

# ANSI codes
RST = "\033[0m" # Reset
BLD = "\033[1m" # Bold
DIM = "\033[2m" # Dim
ITL = "\033[3m" # Italic
UND = "\033[4m" # Underline
BLK = "\033[5m" # Blink
REV = "\033[7m" # Reverse
HID = "\033[8m" # Hidden
STR = "\033[9m" # Strikethrough

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

BRIGHT_BLACK   = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"

BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"

programName = os.path.splitext(os.path.basename(sys.argv[0]))[0]
hT = f"""
{BLD}{BLUE}COMMANDS:{RST}
{BLD}CLEAR | CLS{RST} ---- CLEARS SCREEN!
{BLD}HELP{RST} ----------- PRINTS THIS!
{BLD}EXIT | QUIT{RST} ---- KILLS {programName}.py!
"""

def clear():
    try:
        print("\033[H\033[J", end="")
    except:
        os.system("cls" if os.name == "nt" else "clear")

def append_ht(appendText):
    global hT
    hT += appendText

def close():
    try:
        sys.exit("GOODBYE!")
    except SystemExit:
        print("GOODBYE!")
        os._exit(0)

cmdRegistry = {
    "CLEAR": clear,
    "CLS": clear,
    "HELP": lambda: print(hT),
    "EXIT": close,
    "QUIT": close
}

def showBar(totalSteps=20, delay=0.08):
    for i in range(totalSteps + 1):
        bar = "█" * i + "-" * (totalSteps - i)
        percentage = (i / totalSteps) * 100
        print(f"{GREEN}LOADING [{bar}] {percentage:.0f}%{RST}", end="\r")
        time.sleep(delay)
    print()

def chkcmd(cmd):
    for key, value in cmdRegistry.items():
        if cmd.upper() in key:
            return value