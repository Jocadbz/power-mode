#! /usr/bin/env python3
import sys
import subprocess

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
    print("The current mode is:")
    subprocess.call("powerprofilesctl get", shell=True)
    sys.exit(0)


def trollface():
    troll_face = """
               ⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⠛⠛⠛⠛⠛⣛⣻⣿⣿⣿⣿⣿⣟⣛⣛⣛⠛⠒⠲⠶⠦⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠁⠀⠀⢀⣤⠶⣛⣩⣥⠤⠤⠤⠤⢤⣤⣤⣭⣭⣉⣉⣛⣛⣻⣭⣥⠬⡍⠛⢶⣄⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⣾⠃⠀⠀⣠⡶⢋⡵⢛⡩⠵⠒⠒⠒⠒⠢⡀⠀⠀⠀⠀⠀⢀⣠⠤⠤⠤⢤⣄⠀⠀⠀⠉⠻⣆⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠘⢁⡴⢋⣴⢿⠒⠈⠉⣏⠉⠐⠒⡾⣄⠀⠀⠀⠀⠀⡠⠀⠀⢀⣀⣈⣙⣆⡀⠀⠀⢹⡆⠀
    ⠀⠀⠀⠀⠀⣠⣾⠃⠀⠀⠀⠀⠀⢀⠟⣁⠀⠁⢀⣤⣦⣤⡀⠘⠀⢈⣷⡄⠀⠀⠀⣇⠖⠉⠙⠅⠀⠀⠉⠉⠑⢦⡈⣷⡀
    ⠀⠀⠀⢠⣾⢿⣧⠤⠤⠤⠄⠀⠖⣿⠀⠃⠀⠀⣿⣿⣿⣿⡗⠀⠐⠁⢸⡇⠀⣀⣰⠉⠠⠀⠀⣰⣶⣷⣶⠀⠀⠀⢱⡈⢻⣦⠀⠀⠀
    ⠀⠀⣠⡿⣱⠋⢀⣴⠶⠚⠻⢶⣤⡘⢧⣄⠆⠂⠀⡉⠉⣉⣀⣀⠉⣠⡟⠁⠀⠉⢻⣆⠀⠀⠀⠘⠛⠟⠛⠀⠀⢈⡿⢍⢢⢹⡇⠀⠀
    ⠀⢠⣿⠁⡇⢠⣿⠁⠀⢰⣦⡀⠉⠉⠀⠈⠙⠲⠾⠾⠶⠶⠶⠚⠋⠉⠀⠀⠀⠀⢸⣯⡑⠢⢤⣀⣂⣀⣨⠤⠒⠛⠃⠘⡆⡇⡧⠀⠀
    ⠀⢸⣿⠀⡇⢸⡇⢠⣴⣾⠋⠛⢷⣦⣀⠀⠀⠀⠠⠤⠤⠴⢠⠶⠒⠀⠀⠀⠀⠀⠀⠉⢿⣦⡀⠀⠀⠀⠀⢸⣷⠀⠀⡼⢡⢣⡇⠀⠀
    ⠀⠀⢿⡇⣧⠘⠿⠀⠀⠸⣧⡀⠀⠈⢻⡿⢶⣦⣄⡀⠀⠀⠸⣆⠐⠟⠻⠷⠀⠀⠀⢀⣾⠛⠃⠑⠤⠀⢀⣼⣿⡇⢀⠤⢂⣾⠃⠀⠀
    ⠀⠀⠈⢻⣌⠑⠦⠀⠀⠀⢿⣿⣷⣤⣸⣷⡀⠀⠈⠙⠻⢿⣶⣤⣄⣀⡀⠀⠀⠙⠿⠟⠁⠀⠀⢀⣠⡴⣿⠉⣿⣿⠀⠀⣼⠁⠀⠀⠀
    ⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⣼⠁⠀⠈⠉⠙⣿⠛⠛⠻⢿⠿⠛⠛⢻⡇⠀⢸⡀⣹⣿⠀⠀⡏
    ⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣄⣀⣿⣄⣀⣀⣸⣄⣀⣠⣴⣿⣶⣿⣿⣿⣿⡇⠀⡇
    ⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇
    ⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠘⣿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣷
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠘⢷⡀⠘⡟⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠻⣾⡃⠀⠀⠈⠙⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣄⠈⠻⣦⡀⠀⠀⡼⠀⠀⠈⠙⠻⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣹⠇⠀⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠈⠛⠷⣼⣇⡀⠀⠀⠀⠀⣿⠀⠀⠀⢸⡇⠀⠀⡿⠀⢸⠇⣘⣧⠟⠀⢀⡿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⡀⠀⠙⠻⠷⠶⣶⣾⣿⣤⣀⣠⣿⣄⣀⣴⠷⠶⠿⠿⠟⠋⠀⢀⣾⠃
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⡤⠞⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀
               """
    print(troll_face)


def power_mode():
    prompt1 = """

[x] Power Mode
[ ] Balanced Mode
[ ] Power-Saving Mode

Power-mode selected.
    """
    subprocess.run("powerprofilesctl performance", shell=True)
    print(prompt1)
    sys.exit(0)


def balanced_mode():
    prompt2 = """

[ ] Power Mode
[x] Balanced Mode
[ ] Power-Saving Mode

Balanced mode selected.
    """
    subprocess.call("powerprofilesctl balanced", shell=True)
    print(prompt2)
    sys.exit(0)


def saving_mode():
    prompt3 = """

[ ] Power Mode
[ ] Balanced Mode
[x] Power-Saving Mode

Power-saving mode selected.
    """
    subprocess.call("powerprofilesctl power-saver", shell=True)
    print(prompt3)
    sys.exit(0)


version = "Version 1.0.1"

abbreviationsDict = {"power": power_mode, "balanced": balanced_mode,
                     "saving": saving_mode, "trollface": trollface}


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
