# -*- coding: UTF-8 -*-
"""Collect up the functons used in all the weeks."""
from colorama import Fore
from colorama import Style
import imp
import inspect
import os
import signal
import subprocess
import threading


class RunCmd(threading.Thread):
    """Run a subprocess command, if it exceeds the timeout kill it.

    (without mercy)
    """

    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = subprocess.Popen(self.cmd)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()  # use self.p.kill() if process needs a kill -9
            self.join()


class Timeout():
    """Timeout class using ALARM signal."""

    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout("Timeout: you took toooo damn long!")


def test(testResult, name):
    """Report on the test.

    Returns 1 and 0 so that the 1s can be summed to give a mark.
    """
    if testResult:
        print(Fore.GREEN + "✔ " + name + Style.RESET_ALL)
        return 1
    else:
        print(Fore.RED + "✘ " + name + Style.RESET_ALL)
        return 0


def test_flake8(fileName):
    """Check to see if the file at file_path is flake8 compliant."""
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


def test_pydocstyle(fileName, flags="-e"):
    """Check to see if the file at file_path is pydocstyle compliant."""
    test_dir = os.path.dirname(os.path.abspath(inspect.getfile(
        inspect.currentframe())))

    file_path = os.path.join(test_dir, fileName)
    print(file_path)
    try:
        child = subprocess.Popen(["pydocstyle", file_path, flags],
                                 stdout=subprocess.PIPE)
        streamdata = child.communicate()[0]
        print("streamdata", streamdata)  # I don't know what streamdata is for
        rc = child.returncode
        print("returncode", rc)
        if rc == 0:
            print("all good")
            return True
        elif rc is None:
            print("all good, I think")
            return True
        else:
            print("U haz docstring errorz" + grumpy())
            return False
    except Exception as e:
        print("failed to doc check", e)
        return False


def ex_runs(path, exNumber, weekNumber):
    """Check that this exercise runs at all."""
    try:
        path = "{}/week{}/exercise{}.py".format(path, weekNumber, exNumber)
        imp.load_source("exercise{}".format(exNumber), path)
        return True
    except Exception as e:
        syntax_error_message(exNumber, e)
        return False


def syntax_error_message(exNumber, e):
    """Give a readable error message."""
    print('\n{s:{c}^{n}}\n{s:{c}^{n}}'.format(n=50, c='*', s=""))
    print("There is a syntax error in exercise{}\n{}".format(exNumber, str(e)))
    print("WARNING: there might be more tests, but they won't run")
    print("until you fix the syntax errors in exercise{}.py".format(exNumber))
    print('{s:{c}^{n}}\n{s:{c}^{n}}\n'.format(n=50, c='*', s=""))


def completion_message(message, width):
    u"""Print an obvious message.

    Example:
    In [5]: completion_message("this is the message", 30)
    ******************************

    ✔ this is the message

    ******************************
    """
    cap = '{start}{s:{c}^{n}}{end}'.format(n=width, c='*', s="",
                                           start=Fore.GREEN,
                                           end=Style.RESET_ALL)
    print cap + "\n"
    print(Fore.GREEN + "✔ " + message + Style.RESET_ALL)
    print "\n" + cap


def nyan_cat(block='█'):
    """Return a coloured string that shows a nyan cat."""
    c = [
         ['{BRIGHT_BLUE}', '{x}'*80],
         ['{BRIGHT_BLUE}', '{x}'*80],
         ['{RED}', '{x}'*18, '{BRIGHT_BLUE}', '{x}'*16, '{BLACK}',
          '{x}'*30, '{BRIGHT_BLUE}', '{x}'*16],
         ['{RED}', '{x}'*32, '{BLACK}{x}{x}{WHITE}', '{x}'*30,
          '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*14],
         ['{BRIGHT_RED}', '{x}'*4, '{RED}', '{x}'*26, '{BLACK}{x}{x}{WHITE}',
          '{x}'*6, '{MAGENTA}', '{x}'*22, '{WHITE}', '{x}'*6,
          '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*12],
         ['{BRIGHT_RED}', '{x}'*30, '{BLACK}{x}{x}{WHITE}', '{x}'*4,
          '{MAGENTA}', '{x}'*16, '{BLACK}', '{x}'*4, '{MAGENTA}',
          '{x}'*6, '{WHITE}', '{x}'*4,
          '{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}{BLACK}', '{x}'*4, '{BRIGHT_BLUE}',
          '{x}'*6],
         ['{BRIGHT_RED}', '{x}'*30, '{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}',
          '{x}'*16, '{BLACK}{x}{x}{WHITE}', '{x}'*4, '{BLACK}{x}{x}{MAGENTA}',
          '{x}'*6, '{WHITE}{x}{x}{BLACK}', '{x}'*4, '{WHITE}', '{x}'*4,
          '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*4],
         ['{BRIGHT_YELLOW}', '{x}'*18, '{BRIGHT_RED}', '{x}'*12,
          '{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}', '{x}'*16,
          '{BLACK}{x}{x}{WHITE}', '{x}'*6, '{MAGENTA}', '{x}'*6,
          '{WHITE}{x}{x}{BLACK}{x}{x}{WHITE}', '{x}'*6,
          '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*4],
         ['{BRIGHT_YELLOW}', '{x}'*22, '{BLACK}{x}{x}{BRIGHT_YELLOW}',
          '{x}'*6, '{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}', '{x}'*16,
          '{BLACK}{x}{x}{WHITE}', '{x}'*6, '{BLACK}', '{x}'*8, '{WHITE}',
          '{x}'*8, '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*4],
         ['{BRIGHT_YELLOW}', '{x}'*20,
          '{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}{x}{x}{BRIGHT_YELLOW}', '{x}'*4,
          '{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}', '{x}'*16,
          '{BLACK}{x}{x}{WHITE}', '{x}'*22, '{BLACK}{x}{x}{BRIGHT_BLUE}',
          '{x}'*4],
         ['{BRIGHT_GREEN}', '{x}'*18, '{BRIGHT_YELLOW}{x}{x}{BLACK}',
          '{x}'*2, '{WHITE}{x}{x}{BLACK}', '{x}'*8, '{WHITE}{x}{x}{MAGENTA}',
          '{x}'*14, '{BLACK}{x}{x}{WHITE}', '{x}'*26,
          '{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}'],
         ['{BRIGHT_GREEN}', '{x}'*22, '{WHITE}', '{x}'*8,
          '{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}', '{x}'*14,
          '{BLACK}{x}{x}{WHITE}', '{x}'*6, '{BRIGHT_YELLOW}{x}{x}{WHITE}',
          '{x}'*10, '{BRIGHT_YELLOW}{x}{x}{BLACK}{x}{x}{WHITE}', '{x}'*4,
          '{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}'],
         ['{BRIGHT_GREEN}', '{x}'*22, '{BLACK}', '{x}'*4, '{WHITE}',
          '{x}'*4, '{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}', '{x}'*14,
          '{BLACK}{x}{x}{WHITE}', '{x}'*6, '{BLACK}{x}{x}{WHITE}', '{x}'*6,
          '{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}', '{x}'*4, '{WHITE}', '{x}'*4,
          '{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}'],
         ['{BLUE}', '{x}'*18, '{BRIGHT_GREEN}', '{x}'*8, '{BLACK}',
          '{x}'*6, '{WHITE}{x}{x}{MAGENTA}', '{x}'*14,
          '{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}', '{x}'*4, '{WHITE}', '{x}'*16,
          '{MAGENTA}', '{x}'*4, '{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}'],
         ['{BLUE}', '{x}'*30, '{BLACK}{x}{x}{WHITE}', '{x}'*4, '{MAGENTA}',
          '{x}'*14, '{BLACK}{x}{x}{WHITE}', '{x}'*6, '{BLACK}', '{x}'*12,
          '{WHITE}', '{x}'*4, '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*4],
         ['{BRIGHT_BLUE}', '{x}'*18, '{BLUE}', '{x}'*4, '{BLUE}',
          '{x}'*6, '{BLACK}', '{x}'*4, '{WHITE}', '{x}'*6, '{MAGENTA}',
          '{x}'*14, '{BLACK}{x}{x}{WHITE}', '{x}'*18,
          '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*6],
         ['{BRIGHT_BLUE}', '{x}'*26, '{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}',
          '{x}'*4, '{WHITE}', '{x}'*20, '{BLACK}', '{x}'*18,
          '{BRIGHT_BLUE}', '{x}'*8],
         ['{BRIGHT_BLUE}', '{x}'*24, '{BLACK}{x}{x}{WHITE}', '{x}'*6,
          '{BLACK}', '{x}'*32, '{WHITE}{x}{x}{BLACK}{x}{x}{BRIGHT_BLUE}',
          '{x}'*12],
         ['{BRIGHT_BLUE}', '{x}'*24, '{BLACK}{x}{x}{WHITE}', '{x}'*4,
          '{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}{BLACK}{x}{x}{WHITE}', '{x}'*4,
          '{BRIGHT_BLUE}', '{x}'*12, '{BLACK}{x}{x}{WHITE}', '{x}'*4,
          '{BLACK}', '{x}'*4, '{WHITE}', '{x}'*4,
          '{BLACK}{x}{x}{BRIGHT_BLUE}', '{x}'*12],
         ['{BRIGHT_BLUE}', '{x}'*24, '{BLACK}', '{x}'*6, '{BRIGHT_BLUE}',
          '{x}'*4, '{BLACK}', '{x}'*6, '{BRIGHT_BLUE}', '{x}'*12,
          '{BLACK}', '{x}'*6, '{BRIGHT_BLUE}', '{x}'*4, '{BLACK}',
          '{x}'*6, '{BRIGHT_BLUE}', '{x}'*12],
         ['{x}'*80, '{WHITE}']
    ]
    c = "\n".join(["".join(x) for x in c])
    return c.format(BLACK=Style.NORMAL + "" + Fore.BLACK,
                    BLUE=Style.NORMAL + "" + Fore.BLUE,
                    BRIGHT_BLUE=Style.BRIGHT + "" + Fore.BLUE,
                    BRIGHT_GREEN=Style.BRIGHT + "" + Fore.GREEN,
                    BRIGHT_RED=Style.BRIGHT + "" + Fore.RED,
                    BRIGHT_YELLOW=Style.BRIGHT + "" + Fore.YELLOW,
                    MAGENTA=Style.NORMAL + "" + Fore.MAGENTA,
                    RED=Style.NORMAL + "" + Fore.RED,
                    WHITE=Style.BRIGHT + "" + Fore.WHITE,
                    x=block)


def grumpy():
    """Return a grumpy cat.

    from: http://textart4u.blogspot.com.au/
                 2013/02/grumpy-cat-meme-ascii-text-art.html
    """
    return """
▌▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   ▐█  ▀▀▀▐
▌    ▄                  ▄█▓█▌    ▐
▌   ▐██▄               ▄▓░░▓▓    ▐
▌   ▐█░██▓            ▓▓░░░▓▌    ▐
▌   ▐█▌░▓██          █▓░░░░▓     ▐
▌    ▓█▌░░▓█▄███████▄███▓░▓█     ▐
▌    ▓██▌░▓██░░░░░░░░░░▓█░▓▌     ▐
▌     ▓█████░░░░░░░░░░░░▓██      ▐
▌     ▓██▓░░░░░░░░░░░░░░░▓█      ▐
▌     ▐█▓░░░░░░█▓░░▓█░░░░▓█▌     ▐
▌     ▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌     ▐
▌     ▓▓░▓██████▓░▓███▓▓▌░█▓     ▐
▌    ▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██     ▐
▌    ▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌    ▐
▌    ▓█▌░▓█████▓░░░▓███▓▀░▓█▓    ▐
▌   ▐▓█░░░▀▓██▀░░░░░ ▀▓▀░░▓█▓    ▐
▌   ▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓    ▐
▌   ▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌   ▐
▌   ▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓   ▐
▌  ▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓▌  ▐
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░██▓  ▐
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓  ▐
██████████████████████████████████
█░▀░░░░▀█▀░░░░░░▀█░░░░░░▀█▀░░░░░▀█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░░░░░▄█░░▄▄▄▄▄█
█░░▐█▌░░█░░░██░░░█░░░░████░░░░░░░█
█░░▐█▌░░█▄░░░░░░▄█░░░░████▄░░░░░▄█
██████████████████████████████████"""
