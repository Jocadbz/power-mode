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
<br></br>

## Installation

Package Manager/Binary:
```bash
# On Arch Linux
wget https://jocadbz.github.io/arch-repo/x86_64/power-mode-2.0.0-1-any.pkg.tar.zst
sudo pacman -U power-mode-2.0.0-1-any.pkg.tar.zst

# From binary
wget https://github.com/Jocadbz/power-mode/releases/download/v2.0.0/powermode
sudo mv powermode /usr/bin/
```

From source:
```bash
# You need to install the V compiler
git clone https://github.com/Jocadbz/power-mode.git && cd power-mode/src/
v main.v
```

## Usage

```bash
Usage: powermode [flags] [commands]

CLI tool for powerprofiles ctl

Flags:
  -help               Prints help information.
  -version            Prints version information.

Commands:
  power               Sets Power mode
  balanced            Sets balanced mode
  saving              Sets Power-saving mode
  help                Prints help information.
  version             Prints version information.
```