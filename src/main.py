#! /usr/bin/env python3
import sys
import subprocess
import powerprofiles

app_help = """
Power Mode
Version 1.0.1
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
    sys.exit(0)


def power_mode():
    prompt1 = """

[x] Power Mode
[ ] Balanced Mode
[ ] Power-Saving Mode

Power-mode selected.
    """
    powerprofiles.set_performance()
    print(prompt1)
    sys.exit(0)


def balanced_mode():
    prompt2 = """

[ ] Power Mode
[x] Balanced Mode
[ ] Power-Saving Mode

Balanced mode selected.
    """
    powerprofiles.set_balanced()
    print(prompt2)
    sys.exit(0)


def saving_mode():
    prompt3 = """

[ ] Power Mode
[ ] Balanced Mode
[x] Power-Saving Mode

Power-saving mode selected.
    """
    powerprofiles.set_power_saver()
    print(prompt3)
    sys.exit(0)


version = "Version 1.0.1"

abbreviationsDict = {"power": power_mode, "balanced": balanced_mode,
                     "saving": saving_mode}


def do_work():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        get_mode()
        sys.exit(0)
    else:
        for arguments in args:
            arguments = arguments.lower()
            if arguments == '--help' or arguments == '-h':
                print(app_help)
                sys.exit(0)
            elif arguments == '--version':
                print(version)
                sys.exit(0)
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
