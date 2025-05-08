from src.modules.utils import *
import sys, os, time

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
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('# '):
                        desc = line.lstrip('# ').strip()
                        break
        except Exception as e:
            desc = f"ERROR: CAN'T READ FILE ({str(e)})"
        features.append(f" - {fname} > {desc}")
except FileNotFoundError:
    features = [" - NOTHING HERE BUT US CHICKENS!"]
message = f"""{BLD}{RED}HELLO ZEPP{RST}

{BLD}{CYAN}THIS REPO MAY BE A VOID NOW BUT... TRUST ME, IT'LL {UND}OVERFLOW SOON{RST}{BLD}{CYAN}.{RST}
{BLD}{CYAN}NOTE:{RST} {GREEN}CODES HERE ≈ ZERO-AI; I'M LEARNING PYTHON THROUGH THIS.{RST}
"""

vision = f"""{BLD}{CYAN}VISION:{RST}
{GREEN}{"\n".join(features)}{RST}
"""

goodBye = f"""{BLD}{CYAN}BY:{RST} {GREEN}Ray Cullen{RST} {BRIGHT_BLUE}@{RST} {BLUE}https://github.com/messierCobalt{RST}

{BLD}{RED}GOOD LUCK!{RST}
"""

def main():
    clear()
    showBar(75, 0.01, label="PREPARING README", finishedMsg="READY!")
    time.sleep(0.1)
    clear()

    sections = [message, vision, goodBye]
    for i, content in enumerate(sections):
        slowPrint(content, 0.005, 0.01)
        if i < len(sections) - 1: 
            while True:
                userInput = input(f"\n\n{BRIGHT_CYAN}{BLD}CONTINUE? {RST}").strip()
                if not userInput or userInput.strip().upper() in {"YES", "YEAH", "YEP", "Y", ""}: 
                    break
                cmd = userInput.split()[0].lower()
                func = chkcmd(cmd)
                if func:
                    func()
                else:
                    slowPrint(f"{RED}ERROR!{RST}", 0.005, 0.01)
            clear()

if __name__ == "__main__":
    main()