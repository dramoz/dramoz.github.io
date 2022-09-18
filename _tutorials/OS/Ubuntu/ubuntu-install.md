---
title: Ubuntu 20.04 Install and Setup (Stand-alone or as VM)
tags: ["Install", "Setup"]
superseed: false
icon: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Logo-ubuntu_cof-orange-hex.svg/1200px-Logo-ubuntu_cof-orange-hex.svg.png
favicon: fa-brands fa-ubuntu
---
## Prerequisites

- Intel/AMD amd64/x86 processor (>1GHz, >2GB RAM, >10GB hard drive)

The requirements for any OS vary accordingly to the final use of the desktop. For a more detailed explanation check my post [Workstation Requirements]({% link _blogs/workstation_requirements.md %}).

## Introduction

This is a step-by-step Ubuntu OS installation. It targets Ubuntu 20.04 LTS, but it could work as a guide for other versions.

For a quick - semi-automated installation check [Ubuntu - Quick Install]()

## Installation

1. Download <img src="https://assets.ubuntu.com/v1/8dd99b80-ubuntu-logo14.png" alt="Ubuntu" style="height:25px" /> from [Ubuntu 20.04.4 LTS (Focal Fossa)](https://releases.ubuntu.com/20.04.4/)
   1. <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/computer.svg" alt="desktop" style="height:1.2em;" /> Host: create a bootable USB - you can use [<img src="https://raw.githubusercontent.com/pbatard/rufus/master/res/icons/rufus-128.png" style="height:1.2em" /> Rufus](https://rufus.ie/en/) and enable your BIOS to boot from the USB drive
   2. <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/virtualbox_logo_icon_169253.png" alt="VirtualBox" style="height:1.2em" /> [VirtualBox](https://www.virtualbox.org/): create a new [VM]({% link _tutorials/OS/virtualbox-install.md %}) and under settings add the downloaded ISO file to `Storage > IDE > Choose a disk file`
   3. <img src="https://upload.wikimedia.org/wikipedia/en/7/7d/VMware_Player_logo.png" alt="img" style="height:1.2em;" /> [VMWare Player](https://partnerweb.vmware.com/GOSIG/Ubuntu_20_04_LTS.html) create a new [VM]({% link _tutorials/OS/virtualbox-install.md %})
   
2. Boot or start the VM
3. Run `Install Ubuntu` from the menu
   1. Select Minimal Installation
   2. Add user
   3. Wait

<!-- Add slideshow -->

1. Done!

### First Step

Run VM and log into Ubuntu.

```bash
# right click on the middle of the screen
# -> Open in Terminal
sudo apt update -y; sudo apt upgrade -y; sudo apt autoremove -y; sudo reboot
```

#### Basic R&D setup

```bash
# For USB/UART serial access
sudo adduser $USER dialout

# Dev dirs
cd ~
mkdir -p dev tools repos
```

#### Basic Development Tools & Packages

```bash
# Required apps
sudo apt install -y build-essential git graphviz gtkwave screen tmux tree vim python3 python3-pip python3-tk meld

# Setup git credentials
git config --global user.email "yout@email"
git config --global user.name "Your Name"
```

#### Shortcut

```bash
# To do setup with devsetup scripts
sudo apt install -y git
cd ~/dev
git clone git@github.com:dramoz/devsetup.git
cd ~

# Clone repository with scripts to automate installation
~/dev/devsetup/scripts/ubuntu_setup.sh

# Note: -> split script in two, first install virtualenv, source .bashrc and then do rest
# -> create dev + hdl + ml env separately
~/dev/devsetup/scripts/dev_setup.sh

```

### SSH Keys

#### Add access to **GitHub with SSH key**

```bash
ssh-keygen -t ed25519 -C "your@email"
# Test ssh agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
#Goto: <https://github.com/settings/keys>
```

#### Add access to Azure DevOps **with SSH key**

```bash
ssh-keygen -C "your@email"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
#Goto: <https://COMPANY.visualstudio.com/_usersSettings/keys>
```

### Virtual Machine (Guess)

#### Virtual Box (Guest Additions)

```bash
# From VM menu
# -> Devices.Insert Guest Additions...
# -> Follow instructions

# Restart machine
sudo adduser $USER vboxsf
sudo reboot
```

#### VMWare

```bash
# Mouse wheel fix
sudo apt remove xserver-xorg-input-libinput && sudo apt install xserver-xorg-input-evdev
```



## Setup Development Tools

### Setup Python Virtualenv

```bash
# Python Virtual Env (just in case)
sudo apt purge -y python3-virtualenv
pip3 install virtualenv virtualenvwrapper

# Check paths
which virtualenv
/home/user/.local/bin/virtualenv

# Optional (if using devsetup)
cp ~/dev/devsetup/scripts/.bashrc ~/
source ~/.bashrc

# ------------------------------------------------------------
# Alternative:
# Update .bashrc accordingly
echo '# virtualenv and virtualenvwrapper' >> ~/.bashrc
echo 'export WORKON_HOME=${HOME}/.virtualenvs' >> ~/.bashrc
echo 'export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3' >> ~/.bashrc
echo 'export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv' >> ~/.bashrc
echo 'source $HOME/.local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
# ------------------------------------------------------------
```

### **Cleanup**

```
sudo apt -y update; sudo apt -y upgrade; sudo apt -y autoremove; sudo reboot
```

### Setup dev virtualenv (optional)

```bash
cd ~
mkvirtualenv dev
pip install -r dev/devsetup/virtualenv/full_dev_requirements.txt
```

## Troubleshooting

* `ping name.local` not working (bonjour)
  ```bash
  # Test 
  sudo systemctl status avahi-daemon
  # -> shows "Active: starting up..." (permanently)
  sudo apt purge avahi-daemon
  sudo reboot
  sudo apt install avahi-daemon
  sudo systemctl status avahi-daemon
  # -> should show now "Active: active (running)"
  ```

# Additional settings

`Open Settings` (left click on power icon - top right corner, `> Settings`)

* `Power > Blanc Screen: Never`

# Useful Apps (optional)

Open **Ubuntu Software App** and install:

* **Visual Code** : it takes some time as it has to install snap first
* **Brave** : web browser (enable sync)
* [pyGrid](https://github.com/pkkid/pygrid)

> 💡 Don’t forget right click on the app, `Add tofavouritess`

# Gnome Extensions (optional)

```bash
sudo apt install gnome-shell-extensions chrome-gnome-shell
firefox --new-window <https://extensions.gnome.org/> &
```

> Install Gnome Shell Extension (firefox plugin)
> 💡[Click here to install browser extension](https://extensions.gnome.org/#).
> Reload webpage

## Extensions

> Open `Tweaks` App and click `Extensions` from applications to change extensions settings

* [<img src="https://extensions.gnome.org/extension-data/icons/icon_1160_AXIRYp2.png" style="height:1.2em;" />Dash to Panel](https://extensions.gnome.org/extension/1160/dash-to-panel/), setup:
  * `Position > PanelThickness: 32px`
  * `Position > ActivitiesButton: Enable`
  * `Behavior > ShowFavoriteApplications: Disable`
* [<img src="https://extensions.gnome.org/static/images/plugin.png" style="height:1.2em;" />Favorites Menu](https://extensions.gnome.org/extension/115/favorites-menu/)
* [<img src="https://extensions.gnome.org/extension-data/icons/icon_7.png" style="height:1.2em;" />Removable Drive Menu](https://extensions.gnome.org/extension/7/removable-drive-menu/)
* [<img src="https://extensions.gnome.org/extension-data/icons/icon_21.png" style="height:1.2em;" />Workspace Indicator](https://extensions.gnome.org/extension/21/workspace-indicator/)
* [<img src="https://extensions.gnome.org/extension-data/icons/icon_8.png" style="height:1.2em;" />Places Status Indicator](https://extensions.gnome.org/extension/8/places-status-indicator/)
* [<img src="https://extensions.gnome.org/extension-data/icons/icon_1634_jvSXMcs.png" style="height:1.2em;" />Resource Monitor](https://extensions.gnome.org/extension/1634/resource-monitor/)

# Other Apps

[balenaEtcher - Flash OS images to SD cards &amp; USB drives](https://www.balena.io/etcher/)

* [Jekyll (GitHub Pages)](https://jekyllrb.com/docs/installation/ubuntu/) (**Free hosting** with GitHub Pages)
  [GitHub Pages](https://pages.github.com/)

  ```bash
  # Install dependencies
  sudo apt-get install ruby-full build-essential zlib1g-dev
  
  # Update .bashrc for Gems directory
  echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
  echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
  echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
  
  # install
  gem install jekyll bundler
  ```
  Simple website

  ```bash
  # Create new website
  cd ~/dev
  jekyll new myblog
  cd myblog
  
  # Run in background
  screen -S myblog_dev
  bundle exec jekyll serve --livereload
  # ctrl + a, d  (detach screen session)
  
  # Load website
  firefox <http://127.0.0.1:4000/> &
  ```
