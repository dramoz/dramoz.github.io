---
title: Ubuntu 20.04 Install and Setup
tags: ["OS", "Ubuntu", "Install"]
icon: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Logo-ubuntu_cof-orange-hex.svg/1200px-Logo-ubuntu_cof-orange-hex.svg.png
---
## Prerequisites



## Install

1. Download Ubuntu from [](https://ubuntu.com/download/desktop)[https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
2. In VM under settings add ISO file to `Storage > IDE > Choose a disk file`
3. Start VM
4. Run `Install Ubuntu` from the menu
   1. Select Minimal Installation
   2. Add user
   3. Wait
5. Done!

### First Step

Run VM and log into Ubuntu.

```bash
# right click on middle of the screen
# -> Open in Terminal
sudo apt update -y; sudo apt upgrade -y; sudo apt autoremove -y; sudo reboot
```

Basic R&D setup

```bash
# For USB/UART serial access
sudo adduser $USER dialout

# Dev dirs
cd ~
mkdir -p dev tools repos
```

### Add access to **GitHub with SSH key**

```bash
ssh-keygen -t ed25519 -C "your@email"
# Test ssh agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
#Goto: <https://github.com/settings/keys>

# Optional
cd ~/dev
git clone git@github.com:dramoz/devsetup.git
```

### Add access to Azure DevOps **with SSH key**

```bash
ssh-keygen -C "your@email"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
#Goto: <https://COMPANY.visualstudio.com/_usersSettings/keys>
```

### Install Guest Additions (VM menu)

```bash
# From VM menu
# -> Devices.Insert Guest Additions...
# -> Follow instructions

# Restart machine
sudo adduser $USER vboxsf
sudo reboot
```

# Setup Basic Development Tools

```bash
# Purge some stuff as required (VM Ubuntu)
sudo apt purge -y avahi-daemon

# Required apps
sudo apt install -y build-essential git graphviz gtkwave screen tmux tree vim python3 python3-pip python3-tk meld avahi-daemon

# Setup git credentials
git config --global user.email "yout@email"
git config --global user.name "Your Name"
```

## Setup Python Virtualenv

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

## **Cleanup**

```
sudo apt -y update; sudo apt -y upgrade; sudo apt -y autoremove; sudo reboot
```

## Setup dev virtualenv (optional)

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
* **Typora** : WYSIWYG markdown editor (requires pay license)

<aside>
💡 Don’t forget right click on the app, `Add to favorites`

</aside>

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

* [Dash to Panel](https://extensions.gnome.org/extension/1160/dash-to-panel/), setup:
  * `Position > PanelThickness: 32px`
  * `Position > ActivitiesButton: Enable`
  * `Behavior > ShowFavoriteApplications: Disable`
* [Favorites Menu](https://extensions.gnome.org/extension/115/favorites-menu/)
* [gTile](https://extensions.gnome.org/extension/28/gtile/)
* [Removable Drive Menu](https://extensions.gnome.org/extension/7/removable-drive-menu/)
* [Workspace Indicator](https://extensions.gnome.org/extension/21/workspace-indicator/)
* [Places Status Indicator](https://extensions.gnome.org/extension/8/places-status-indicator/)

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
