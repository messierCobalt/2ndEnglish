import os, sys, time, random

RST = "\033[0m"  # Reset
BLD = "\033[1m"  # Bold
DIM = "\033[2m"  # Dim
ITL = "\033[3m"  # Italic
UND = "\033[4m"  # Underline
BLK = "\033[5m"  # Blink
REV = "\033[7m"  # Reverse
HID = "\033[8m"  # Hidden
STR = "\033[9m"  # Strikethrough

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

programName = os.path.splitext(os.path.basename(sys.argv[0]))[0]

hT = f"""
{BLD}{BLUE}COMMANDS:{RST}
{BLD}CLEAR | CLS | CLEAN{RST} ---- CLEARS SCREEN!
{BLD}HELP | GUIDE | MANUAL{RST} --- PRINTS THIS!
{BLD}EXIT | QUIT | CLOSE{RST} ---- KILLS {programName}.py!
"""

append_hT = lambda hT, appendTxt: hT + appendTxt

clear = lambda: os.system("cls" if os.name == "nt" else "clear")
close = lambda: sys.exit(f"{GREEN}GOODBYE!{RST}")
helper = lambda: print(hT)

cmdRegistry = {
    ("CLEAR", "CLS", "CLEAN"): clear,
    ("HELP", "GUIDE", "MANUAL"): helper,
    ("EXIT", "QUIT", "CLOSE"): close
}

def append_cR(cmd, func):
    cmdRegistry[cmd] = func

def showBar(totalSteps=25, delay=0.05, label=f"LOADING {programName}.py", finishedMsg="READY!", color=GREEN):
    for i in range(totalSteps + 1):
        bar = "█" * i + "-" * (totalSteps - i)
        percent = f"{(i / totalSteps) * 100:.0f}%".rjust(4)
        if i == totalSteps and finishedMsg:
            print(f"\r{color}{label} [{bar}] {percent} {finishedMsg}{RST}", end="", flush=True)
        else:
            print(f"\r{color}{label} [{bar}] {percent}{RST}", end="", flush=True)
        time.sleep(delay)
    print()

def chkcmd(cmd):
    cmd = cmd.upper()
    for key, func in cmdRegistry.items():
        if isinstance(key, tuple) and cmd in key:
            return func
        elif cmd == key:
            return func
    return None

def slowPrint(text, minT=0.01, maxT=0.05):
    """Print text slowly with random delays between characters."""
    for char in text:
        time.sleep(random.uniform(minT, maxT))
        print(char, end="", flush=True)