# -*- coding: UTF-8 -*-
from colorama import Fore, Style
import inspect
import os


def test(testResult, name):
    if testResult:
        print(Fore.GREEN + "✔ " + name + Style.RESET_ALL)
        return 1
    else:
        print(Fore.RED + "✘ " + name + Style.RESET_ALL)
        return 0


def test_flake8(fileName):
    test_dir = os.path.dirname(os.path.abspath(inspect.getfile(
        inspect.currentframe())))

    files = [os.path.join(test_dir, fileName)]
    # Import the legacy API as flake8 3.0 currently has no official
    # public API - this has to be changed at some point.
    from flake8.api import legacy as flake8
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files(files)

    if report.total_errors == 0:
        return True
    else:
        print report.total_errors
        return False


def completion_message(message, width):
    cap = '{start}{s:{c}^{n}}{end}'.format(n=width, c='*', s="",
                                           start=Fore.GREEN,
                                           end=Style.RESET_ALL)
    print cap + "\n"
    print(Fore.GREEN + "✔ " + message + Style.RESET_ALL)
    print "\n" + cap

def nyan_cat():
    return "\n".join([
    "{BRIGHT_BLUE}████████████████████████████████████████████████████████████████████████████████",
    "{BRIGHT_BLUE}████████████████████████████████████████████████████████████████████████████████",
    "{RED}██████████████████{BRIGHT_BLUE}████████████████{BLACK}██████████████████████████████{BRIGHT_BLUE}████████████████",
    "{RED}████████████████████████████████{BLACK}██{WHITE}██████████████████████████████{BLACK}██{BRIGHT_BLUE}██████████████",
    "{BRIGHT_RED}████{RED}██████████████████████████{BLACK}██{WHITE}██████{MAGENTA}██████████████████████{WHITE}██████{BLACK}██{BRIGHT_BLUE}████████████",
    "{BRIGHT_RED}██████████████████████████████{BLACK}██{WHITE}████{MAGENTA}████████████████{BLACK}████{MAGENTA}██████{WHITE}████{BLACK}██{BRIGHT_BLUE}██{BLACK}████{BRIGHT_BLUE}██████",
    "{BRIGHT_RED}██████████████████████████████{BLACK}██{WHITE}██{MAGENTA}████████████████{BLACK}██{WHITE}████{BLACK}██{MAGENTA}██████{WHITE}██{BLACK}████{WHITE}████{BLACK}██{BRIGHT_BLUE}████",
    "{BRIGHT_YELLOW}██████████████████{BRIGHT_RED}████████████{BLACK}██{WHITE}██{MAGENTA}████████████████{BLACK}██{WHITE}██████{MAGENTA}██████{WHITE}██{BLACK}██{WHITE}██████{BLACK}██{BRIGHT_BLUE}████",
    "{BRIGHT_YELLOW}██████████████████████{BLACK}██{BRIGHT_YELLOW}██████{BLACK}██{WHITE}██{MAGENTA}████████████████{BLACK}██{WHITE}██████{BLACK}████████{WHITE}████████{BLACK}██{BRIGHT_BLUE}████",
    "{BRIGHT_YELLOW}████████████████████{BLACK}██{WHITE}██{BLACK}██{BRIGHT_YELLOW}████{BLACK}██{WHITE}██{MAGENTA}████████████████{BLACK}██{WHITE}██████████████████████{BLACK}██{BRIGHT_BLUE}████",
    "{BRIGHT_GREEN}██████████████████{BRIGHT_YELLOW}██{BLACK}██{WHITE}██{BLACK}████████{WHITE}██{MAGENTA}██████████████{BLACK}██{WHITE}██████████████████████████{BLACK}██{BRIGHT_BLUE}██",
    "{BRIGHT_GREEN}██████████████████████{WHITE}████████{BLACK}██{WHITE}██{MAGENTA}██████████████{BLACK}██{WHITE}██████{BRIGHT_YELLOW}██{WHITE}██████████{BRIGHT_YELLOW}██{BLACK}██{WHITE}████{BLACK}██{BRIGHT_BLUE}██",
    "{BRIGHT_GREEN}██████████████████████{BLACK}████{WHITE}████{BLACK}██{WHITE}██{MAGENTA}██████████████{BLACK}██{WHITE}██████{BLACK}██{WHITE}██████{BLACK}██{WHITE}██{BLACK}████{WHITE}████{BLACK}██{BRIGHT_BLUE}██",
    "{BLUE}██████████████████{BRIGHT_GREEN}████████{BLACK}██████{WHITE}██{MAGENTA}██████████████{BLACK}██{WHITE}██{MAGENTA}████{WHITE}████████████████{MAGENTA}████{BLACK}██{BRIGHT_BLUE}██",
    "{BLUE}██████████████████████████████{BLACK}██{WHITE}████{MAGENTA}██████████████{BLACK}██{WHITE}██████{BLACK}████████████{WHITE}████{BLACK}██{BRIGHT_BLUE}████",
    "{BRIGHT_BLUE}██████████████████{BLUE}████{BLUE}██████{BLACK}████{WHITE}██████{MAGENTA}██████████████{BLACK}██{WHITE}██████████████████{BLACK}██{BRIGHT_BLUE}██████",
    "{BRIGHT_BLUE}██████████████████████████{BLACK}██{WHITE}██{BLACK}████{WHITE}████████████████████{BLACK}██████████████████{BRIGHT_BLUE}████████",
    "{BRIGHT_BLUE}████████████████████████{BLACK}██{WHITE}██████{BLACK}████████████████████████████████{WHITE}██{BLACK}██{BRIGHT_BLUE}████████████",
    "{BRIGHT_BLUE}████████████████████████{BLACK}██{WHITE}████{BLACK}██{BRIGHT_BLUE}██{BLACK}██{WHITE}████{BRIGHT_BLUE}████████████{BLACK}██{WHITE}████{BLACK}████{WHITE}████{BLACK}██{BRIGHT_BLUE}████████████",
    "{BRIGHT_BLUE}████████████████████████{BLACK}██████{BRIGHT_BLUE}████{BLACK}██████{BRIGHT_BLUE}████████████{BLACK}██████{BRIGHT_BLUE}████{BLACK}██████{BRIGHT_BLUE}████████████",
    "████████████████████████████████████████████████████████████████████████████████"
    ]).format(BLACK=Style.NORMAL + "" + Fore.BLACK,
              BLUE=Style.NORMAL + "" + Fore.BLUE,
              BRIGHT_BLUE=Style.BRIGHT + "" + Fore.BLUE,
              BRIGHT_GREEN=Style.BRIGHT + "" + Fore.GREEN,
              BRIGHT_RED=Style.BRIGHT + "" + Fore.RED,
              BRIGHT_YELLOW=Style.BRIGHT + "" + Fore.YELLOW,
              MAGENTA=Style.NORMAL + "" + Fore.MAGENTA,
              RED=Style.NORMAL + "" + Fore.RED,
              WHITE=Style.BRIGHT + "" + Fore.WHITE)
