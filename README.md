<h1 align="center"><code>Power Mode</code></h1>
<p align="center">CLI tool for Power Profiles Daemon</p>

<p align="center">
<a href="Power Mode.svg">
  <img src="Power Mode.svg">
</a>
</p>

## Dependencies
- power-profiles-daemon
- powerprofilesctl
- python3
<br></br>

## Installation

Package Manager/Binary:
```bash
# On Arch Linux
wget https://jocadbz.github.io/arch-repo/x86_64/power-mode-1.0.0-1-any.pkg.tar.zst
sudo pacman -U power-mode-1.0.0-1-any.pkg.tar.zst

# From binary
wget https://github.com/Jocadbz/power-mode/releases/download/v1.0.0/powermode
sudo mv powermode /usr/bin/
```

From source:
```bash
pip install pyinstaller
git clone https://github.com/Jocadbz/power-mode.git && cd power-mode/src/
pyinstaller --onefile main.py
```

## Usage

```bash
powermode [mode]
(Run without arguments to get the current used mode)
    
Modes:
- power
- balanced
- saving
```