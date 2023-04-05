# Xilinx Tools 2021.x

All tools version MUST match:

- Vitis/Vivado
- Petalinux
- Petalinux Board Support Package (BSP)



## Vitis (+Vivado)

[Vitis Guide](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2021_2/ug1400-vitis-embedded.pdf) (Installation includes Vivado)

- [Download](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html): select proper tool version
  - Note: If possible, download the Unified Installer ~80GB


### Prerequisites

```bash
# Prerequisites
mkvirtualenv xilinx
mkdir -p logs/xilinx
sudo dpkg --add-architecture i386
sudo adduser $USER dialout

# Need to set bash as default
sudo dpkg-reconfigure dash
# -> press [No] to switch to bash

# Dependencies
sudo apt install libcanberra-gtk-module libcanberra-gtk-module:i386
```

### Install

```bash
mkdir ~/tools
cd dir_download_location
tar -xvzf Xilinx_Unified_2021.x_1021_0703.tar.gz
cd Xilinx_Unified_2021.x_1021_0703/
# you can run xsetup as sudo if you want a global installation
# if it is just you, do a user installation
# Launch GUI:
./xsetup
# Select only your devices (ZynQ MPSoC, Kria)
# Select DocNav (not required)
# Install under your home directory
# -> /home/dramoz/tools/Xilinx
...
# After installation is complete, DO NOT FORGET:
sudo ~/tools/Xilinx/Vitis/2021.x/scripts/installLibs.sh
```

### Launchers (optional)

-> Can copy from repository [dramoz/devsetup (github.com)](https://github.com/dramoz/devsetup/tree/main/scripts/xilinx)

#### Vitis

```bash
# Vitis launcher
vim vitis.2021.x.sh
->>
#!/bin/bash
source /usr/local/bin/virtualenvwrapper.sh
workon xilinx
source ~/tools/Xilinx/Vitis/2021.x/settings64.sh
vitis &
<<-
chmod +x vitis.2021.x.sh
```

#### Vivado

```bash
# Vviado launcher
mkdir -p logs/xilinx
vim vivado.2021.x.sh
->>
#!/bin/bash
source /usr/local/bin/virtualenvwrapper.sh
workon xilinx
source ~/tools/Xilinx/Vivado/2021.x/settings64.sh
vivado -journal logs/xilinx -log logs/xilinx &
<<-
chmod +x vivado.2021.x.sh
```



## Petalinux (ZynQ+)

[Petalinux Installation Guide](https://www.xilinx.com/content/dam/xilinx/support/documentation/sw_manuals/xilinx2021_2/ug1144-petalinux-tools-reference-guide.pdf)

* [Download](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools.html): select proper tool version
* [Instructions at Hackster.io](https://www.hackster.io/whitney-knitter/installing-vivado-vitis-petalinux-2021-2-on-ubuntu-18-04-0d0fdf)

### Setup Environment

```bash
# Download and run script
cd ~
firefox --new-window https://support.xilinx.com/s/article/73296
chmod +x ~/Downloads/plnx-env-setup.sh
sudo ~/Downloads/plnx-env-setup.sh
```

### TFTP Server

```bash
sudo vim /etc/xinetd.d/tftp
>>
service tftp 
    {
    protocol = udp 
    port = 69 
    socket_type = dgram 
    wait = yes 
    user = nobody 
    server = /usr/sbin/in.tftpd 
    server_args = /tftpboot 
    disable = no
    }

<<
# Create TFTP directory for booting
sudo mkdir /tftpboot; sudo chmod -R 777 /tftpboot; sudo chown -R nobody /tftpboot
# Restart to changes to take effect
sudo /etc/init.d/xinetd stop; sudo /etc/init.d/xinetd start
```

 ### Install Petalinux

```bash
# Setup execution rights and directories
cd download_location
chmod 755 ./petalinux-v2021.x-final-installer.run
mkdir -p ~/tools/Xilinx/Petalinux/v2021.x

# Install Petalinux for ZynQ+
./petalinux-v2021.x-final-installer.run --dir ~/tools/Xilinx/Petalinux/v2021.x --platform aarch64
```

### Required upgrade

```bash
# get path to right petalinux version (:proper_link)
firefox --new-window http://petalinux.xilinx.com/sswreleases/rel-v2021/sdkupdate/ &

# Upgrade
cd ~/tools/Xilinx/Petalinux/v2021.x
source ./settings.sh
petalinux-upgrade -p "aarch64" --wget-args "--wait 1 -nH --cut-dirs=4" -u proper_link
```

### Testing Petalinux

```bash
source ~/tools/Xilinx/Petalinux/v2021.1/settings.sh 
petalinux-util --webtalk off
petalinux-util --webtalk on
```

___

### Creating Petalinux Project (Kria KV260)

#### Tutorials

- Hackster.io [2021.1]([Getting Started with the Kria KV260 in PetaLinux 2021.1 - Hackster.io](https://www.hackster.io/whitney-knitter/getting-started-with-the-kria-kv260-in-petalinux-2021-1-b491fd))
- Hackster.io [2021.2]([Linux Development on the Kria KV260 with PetaLinux 2021.2 - Hackster.io](https://www.hackster.io/whitney-knitter/linux-development-on-the-kria-kv260-with-petalinux-2021-2-65137a))

#### Instructions

- Download [Kria KV260 BSP]([Downloads (xilinx.com)](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools.html))

```bash
# Source settings
source ~/tools/Xilinx/Petalinux/v2021.x/settings.sh 
mkdir -p ~/dev/petalinux/
cd ~/dev/petalinux/

# Create project:
# -> Options: -n dir_name, default is bsp_name
petalinux-create -t project -s /<path to bsp>/
```

*Console output*

```bash
INFO: Create project: 
INFO: Projects: 
INFO: 	* xilinx-k26-som-2021.x  <= OS directory Name
INFO: Has been successfully installed to /home/dramoz/dev/petalinux/
INFO: New project successfully created in /home/dramoz/dev/petalinux/
```

OS directory name: `xilinx-k26-som-2021.x`

```bash
cd os_directory

# Add Board Variant to K26-SOM
vim project-spec/meta-user/conf/petalinuxbsp.conf
>> key: INS
BOARD_VARIANT = "kv"
<< key: ESC
<< :wq

# Build petalinux
petalinux-build
```