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
    cap = '{start}{s:{c}^{n}}{end}'.format(n=width, c='*', s="", start=Fore.GREEN, end=Style.RESET_ALL)
    print cap + "\n"
    print(Fore.GREEN + "✔ " + message + Style.RESET_ALL)
    print "\n" + cap
