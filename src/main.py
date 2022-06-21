#! /usr/bin/env python3
from sys import argv, exit
import powerprofiles
from rich import print as rprint
from rich.markdown import Markdown

app_help = """
Power Mode
Version 1.1.0
Jocadbz, 2022


Usage:
powermode [mode]
(Run without arguments to get the current used mode)

Modes:
- power
- balanced
- saving
       """


def get_mode():
    print(f"The current mode is: {powerprofiles.get()}")
    exit(0)


def power_mode():
    prompt1 = """
- [x] Power Mode
- [ ] Balanced Mode
- [ ] Power-Saving Mode

    """
    powerprofiles.set_performance()
    md = Markdown(prompt1)
    rprint(md)
    rprint("[red]Power-mode[/red] selected.")
    exit(0)


def balanced_mode():
    prompt2 = """
- [ ] Power Mode
- [x] Balanced Mode
- [ ] Power-Saving Mode

    """
    powerprofiles.set_balanced()
    md = Markdown(prompt2)
    rprint(md)
    rprint("[yellow]Balanced[/yellow] mode selected.")
    exit(0)


def saving_mode():
    prompt3 = """
- [ ] Power Mode
- [ ] Balanced Mode
- [x] Power-Saving Mode

    """
    powerprofiles.set_power_saver()
    md = Markdown(prompt3)
    rprint(md)
    rprint("[green]Power-saving[/green] mode selected.")
    exit(0)


version = "Version 1.1.0"

abbreviationsDict = {"power": power_mode, "balanced": balanced_mode,
                     "saving": saving_mode}


def do_work():
    """ Function to handle command line usage"""
    args = argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        get_mode()
        exit(0)
    else:
        for arguments in args:
            arguments = arguments.lower()
            if arguments == '--help' or arguments == '-h':
                print(app_help)
                exit(0)
            elif arguments == '--version':
                print(version)
                exit(0)
            else:
                try:
                    # Get your function based on key in abbreviationsDict
                    language_required = abbreviationsDict[arguments]
                    language_required()  # Execute this function.
                except KeyError:
                    print(f'Unrecognized Argument: {arguments}.')
                    print("Run 'powermode --help' to see supported functions")


if __name__ == '__main__':
    do_work()
