// Functions
module function

import os

// Performance mode
pub fn performance() {
	println("- [x] Power Mode
- [ ] Balanced Mode
- [ ] Power-Saving Mode

Power-mode selected")
    os.system("powerprofilesctl set performance")
}

// Balanced mode
pub fn balanced() {
    println("- [ ] Power Mode
- [x] Balanced Mode
- [ ] Power-Saving Mode

Balanced mode selected")
    os.system("powerprofilesctl set balanced")
}

// Saving mode
pub fn power_saver() {
    println("- [ ] Power Mode
- [ ] Balanced Mode
- [x] Power-Saving Mode

Power-saving mode selected")
    os.system("powerprofilesctl set power-saver")
}


pub fn get_mode() {
    println('Your current mode is:')
    os.system("powerprofilesctl get")
}


pub fn help() {
    println("Power Mode
Version 1.1.0
Jocadbz, 2022

Usage:
powermode [mode]
(Run without arguments to get the current used mode)

Modes:
- power
- balanced
- saving")
}