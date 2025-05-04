from src.modules.utils import *
import sys, os, random, time

currentDir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(currentDir, "src", "modules"))

srcDir = os.path.join(currentDir, "src")
features = []
try:
    for fname in sorted(os.listdir(srcDir)):
        if not fname.endswith('.py'):
            continue
        path = os.path.join(srcDir, fname)
        desc = "DESCRIPTION NOT FOUND"
        try:
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('# '):
                        desc = line.lstrip('# ').strip()
                        break
        except Exception:
            desc = "ERROR: CAN'T READ FILE(S)"
        features.append(f"{len(features)+1}. {fname} -> {desc}")
except FileNotFoundError:
    features = ["1. NOTHING HERE BUT US CHICKENS!"]

msg = f"""{BLD}{GREEN}README.py from{RST} {BLUE}https://github.com/messierCobalt/secondEnglish{RST}

{BLD}{RED}HELLO ZEPP{RST}

{BLD}{CYAN}THIS REPO MAY BE A VOID NOW BUT... TRUST ME, IT'LL {UND}OVERFLOW SOON{RST}{BLD}{CYAN}.{RST}
{BLD}{CYAN}SIDE NOTE:{RST} {GREEN}CODES HERE ≈ ZERO-AI; I'M LEARNING PYTHON THROUGH THIS.{RST}
{BLD}{CYAN}CURRENT STATUS:{RST} {GREEN}IN BLUEPRINTS{RST}
{BLD}{CYAN}THE VISION:{RST}
{GREEN}{"\n".join(features)}{RST}

{BLD}{CYAN}BY:{RST} {GREEN}Ray Cullen{RST} {BRIGHT_BLUE}@{RST} {BLUE}https://www.github.com/messierCobalt{RST}

{BLD}{RED}GOOD LUCK!{RST}
"""

clear()
showBar()
time.sleep(0.5)
clear()

for char in msg:
    time.sleep(random.uniform(0.0001, 0.05))
    print(char, end="", flush=True)
