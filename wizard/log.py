from rich import print
LIGHT_BLUE = "#7EBAE4"
LIGHT_RED = "#e47e7e"
LIGHT_YELLOW = "#e4d97e"
LIGHT_GREEN = "#7ee48e"
LIGHT_PURPLE = "#bd7ee4"
DARK_BLUE = "#5277C3"
NIXOS_LOGO = ""
COLORED_LOGO = f"[{DARK_BLUE}]{NIXOS_LOGO}[/]"

def banner():
    print(f"[{LIGHT_GREEN}]   nixos-wizard[/] [{LIGHT_PURPLE}]v0.1.0[/]")

def info(msg: str, *args, **kwargs):
    print(f"[{LIGHT_BLUE}]  [/] {COLORED_LOGO} " + msg, *args, **kwargs)

def error(msg: str, *args, **kwargs):
    print(f"[{LIGHT_RED}]  [/] {COLORED_LOGO} " + msg, *args, **kwargs)

def warning(msg: str, *args, **kwargs):
    print(f"[{LIGHT_YELLOW}]  [/] {COLORED_LOGO} " + msg, *args, **kwargs)

def success(msg: str, *args, **kwargs):
    print(f"[{LIGHT_GREEN}] 󰐕 [/] {COLORED_LOGO} " + msg, *args, **kwargs)

def yesno(msg: str, *args, **kwargs) -> bool:
    print(f"[{LIGHT_PURPLE}]Yy/Nn[/] {COLORED_LOGO} " + msg, end=" ", *args, **kwargs)
    return input().lower().strip() in ["Y", "y"]
