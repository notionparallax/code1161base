# -*- coding: UTF-8 -*-
"""Collect up the functons used in all the weeks."""
from colorama import Fore
from colorama import Style
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
    cattern = [
               ['{BRIGHT_BLUE}', '{x}'*80],
               ['{BRIGHT_BLUE}', '{x}'*80],
               ['{RED}', '{x}'*18, '{BRIGHT_BLUE}', '{x}'*16, '{BLACK}',
                '{x}'*30, '{BRIGHT_BLUE}', '{x}'*16],
               ['{RED}', '{x}'*32, '{BLACK}██{WHITE}', '{x}'*30,
                '{BLACK}██{BRIGHT_BLUE}', '{x}'*14],
               ['{BRIGHT_RED}', '{x}'*4, '{RED}', '{x}'*26, '{BLACK}██{WHITE}',
                '{x}'*6, '{MAGENTA}', '{x}'*22, '{WHITE}', '{x}'*6,
                '{BLACK}██{BRIGHT_BLUE}', '{x}'*12],
               ['{BRIGHT_RED}', '{x}'*30, '{BLACK}██{WHITE}', '{x}'*4,
                '{MAGENTA}', '{x}'*16, '{BLACK}', '{x}'*4, '{MAGENTA}',
                '{x}'*6, '{WHITE}', '{x}'*4, '{BLACK}██{BRIGHT_BLUE}██{BLACK}',
                '{x}'*4, '{BRIGHT_BLUE}', '{x}'*6],
               ['{BRIGHT_RED}', '{x}'*30, '{BLACK}██{WHITE}██{MAGENTA}',
                '{x}'*16, '{BLACK}██{WHITE}', '{x}'*4, '{BLACK}██{MAGENTA}',
                '{x}'*6, '{WHITE}██{BLACK}', '{x}'*4, '{WHITE}', '{x}'*4,
                '{BLACK}██{BRIGHT_BLUE}', '{x}'*4],
               ['{BRIGHT_YELLOW}', '{x}'*18, '{BRIGHT_RED}', '{x}'*12,
                '{BLACK}██{WHITE}██{MAGENTA}', '{x}'*16, '{BLACK}██{WHITE}',
                '{x}'*6, '{MAGENTA}', '{x}'*6, '{WHITE}██{BLACK}██{WHITE}',
                '{x}'*6, '{BLACK}██{BRIGHT_BLUE}', '{x}'*4],
               ['{BRIGHT_YELLOW}', '{x}'*22, '{BLACK}██{BRIGHT_YELLOW}',
                '{x}'*6, '{BLACK}██{WHITE}██{MAGENTA}', '{x}'*16,
                '{BLACK}██{WHITE}', '{x}'*6, '{BLACK}', '{x}'*8, '{WHITE}',
                '{x}'*8, '{BLACK}██{BRIGHT_BLUE}', '{x}'*4],
               ['{BRIGHT_YELLOW}', '{x}'*20,
                '{BLACK}██{WHITE}██{BLACK}██{BRIGHT_YELLOW}', '{x}'*4,
                '{BLACK}██{WHITE}██{MAGENTA}', '{x}'*16, '{BLACK}██{WHITE}',
                '{x}'*22, '{BLACK}██{BRIGHT_BLUE}', '{x}'*4],
               ['{BRIGHT_GREEN}', '{x}'*18, '{BRIGHT_YELLOW}██{BLACK}',
                '{x}'*2, '{WHITE}██{BLACK}', '{x}'*8, '{WHITE}██{MAGENTA}',
                '{x}'*14, '{BLACK}██{WHITE}', '{x}'*26,
                '{BLACK}██{BRIGHT_BLUE}██'],
               ['{BRIGHT_GREEN}', '{x}'*22, '{WHITE}', '{x}'*8,
                '{BLACK}██{WHITE}██{MAGENTA}', '{x}'*14, '{BLACK}██{WHITE}',
                '{x}'*6, '{BRIGHT_YELLOW}██{WHITE}', '{x}'*10,
                '{BRIGHT_YELLOW}██{BLACK}██{WHITE}', '{x}'*4,
                '{BLACK}██{BRIGHT_BLUE}██'],
               ['{BRIGHT_GREEN}', '{x}'*22, '{BLACK}', '{x}'*4, '{WHITE}',
                '{x}'*4, '{BLACK}██{WHITE}██{MAGENTA}', '{x}'*14,
                '{BLACK}██{WHITE}', '{x}'*6, '{BLACK}██{WHITE}', '{x}'*6,
                '{BLACK}██{WHITE}██{BLACK}', '{x}'*4, '{WHITE}', '{x}'*4,
                '{BLACK}██{BRIGHT_BLUE}██'],
               ['{BLUE}', '{x}'*18, '{BRIGHT_GREEN}', '{x}'*8, '{BLACK}',
                '{x}'*6, '{WHITE}██{MAGENTA}', '{x}'*14,
                '{BLACK}██{WHITE}██{MAGENTA}', '{x}'*4, '{WHITE}', '{x}'*16,
                '{MAGENTA}', '{x}'*4, '{BLACK}██{BRIGHT_BLUE}██'],
               ['{BLUE}', '{x}'*30, '{BLACK}██{WHITE}', '{x}'*4, '{MAGENTA}',
                '{x}'*14, '{BLACK}██{WHITE}', '{x}'*6, '{BLACK}', '{x}'*12,
                '{WHITE}', '{x}'*4, '{BLACK}██{BRIGHT_BLUE}', '{x}'*4],
               ['{BRIGHT_BLUE}', '{x}'*18, '{BLUE}', '{x}'*4, '{BLUE}',
                '{x}'*6, '{BLACK}', '{x}'*4, '{WHITE}', '{x}'*6, '{MAGENTA}',
                '{x}'*14, '{BLACK}██{WHITE}', '{x}'*18,
                '{BLACK}██{BRIGHT_BLUE}', '{x}'*6],
               ['{BRIGHT_BLUE}', '{x}'*26, '{BLACK}██{WHITE}██{BLACK}',
                '{x}'*4, '{WHITE}', '{x}'*20, '{BLACK}', '{x}'*18,
                '{BRIGHT_BLUE}', '{x}'*8],
               ['{BRIGHT_BLUE}', '{x}'*24, '{BLACK}██{WHITE}', '{x}'*6,
                '{BLACK}', '{x}'*32, '{WHITE}██{BLACK}██{BRIGHT_BLUE}',
                '{x}'*12],
               ['{BRIGHT_BLUE}', '{x}'*24, '{BLACK}██{WHITE}', '{x}'*4,
                '{BLACK}██{BRIGHT_BLUE}██{BLACK}██{WHITE}', '{x}'*4,
                '{BRIGHT_BLUE}', '{x}'*12, '{BLACK}██{WHITE}', '{x}'*4,
                '{BLACK}', '{x}'*4, '{WHITE}', '{x}'*4,
                '{BLACK}██{BRIGHT_BLUE}', '{x}'*12],
               ['{BRIGHT_BLUE}', '{x}'*24, '{BLACK}', '{x}'*6, '{BRIGHT_BLUE}',
                '{x}'*4, '{BLACK}', '{x}'*6, '{BRIGHT_BLUE}', '{x}'*12,
                '{BLACK}', '{x}'*6, '{BRIGHT_BLUE}', '{x}'*4, '{BLACK}',
                '{x}'*6, '{BRIGHT_BLUE}', '{x}'*12],
               ['{x}'*80, '{WHITE}']
    ]
    cattern = "\n".join(["".join(c) for c in cattern])
    return cattern.format(BLACK=Style.NORMAL + "" + Fore.BLACK,
                          BLUE=Style.NORMAL + "" + Fore.BLUE,
                          BRIGHT_BLUE=Style.BRIGHT + "" + Fore.BLUE,
                          BRIGHT_GREEN=Style.BRIGHT + "" + Fore.GREEN,
                          BRIGHT_RED=Style.BRIGHT + "" + Fore.RED,
                          BRIGHT_YELLOW=Style.BRIGHT + "" + Fore.YELLOW,
                          MAGENTA=Style.NORMAL + "" + Fore.MAGENTA,
                          RED=Style.NORMAL + "" + Fore.RED,
                          WHITE=Style.BRIGHT + "" + Fore.WHITE,
                          x='█')
