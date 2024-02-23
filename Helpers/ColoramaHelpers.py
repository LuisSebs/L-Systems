import colorama
from colorama import Back, Fore, Style

# COLORES
cy = Fore.CYAN
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA
lb = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
lg = Fore.LIGHTGREEN_EX
lm = Fore.LIGHTMAGENTA_EX
ly = Fore.LIGHTYELLOW_EX
lr = Fore.LIGHTRED_EX

def p(s, color = Fore.RESET):
    print(c(s, color))

def c(s, color=Fore.RESET):
    return color + s + color + Fore.RESET