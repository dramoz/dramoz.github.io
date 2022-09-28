---
title: Workstation Requirements - VMs and what PC should I get?
tags: ["Tools", "HW"]
unsplash: 95YRwf6CNw8
unsplash_fit: none
favicon: "fa-solid fa-computer"
favicon_color: gray
posted: 2022-06-27
---

# What hardware do I Need?

One common question when starting computer programming, embedded systems or electronics is *What do I need?* As with any hobby or project, money is required to get started. But you do not need to break the bank.

You can go through some basic explanations, or for the impatience, skip and jump ahead to [Summary](#summary)

## The basics

> ℹ The following are my recommendations based on personal and work experience.
>

Nowadays investing in a good desktop computer is a need. However, one important thing to acknowledge is that you do not need to keep up to date with the latest technology.

Back in the day, it used to be that computer hardware was updated so fast, that a desktop computer was replaced between two or four years (alas, some big companies still replace them every year). Most of this urge was dragged for software requirements like OS, {% glossary EDA%} tools, {% glossary IDE %}, or computer games.

But the truth now is that a good old i5 from 2012 is still a powerful processor capable of doing most of your daily computer tasks and embedded design. Saying so, in the end, it depends on what you are going to do with your desktop.

> ⚠️ If you already have a nice computer capable of running your required tools, do not update unless it is strictly necessary (e.g. computer failure, more RAM required, or similar)

## A good processor is good but...

**RAM**, one of the most important things on a computer (laptop or desktop) is the amount of available RAM. The amount of available RAM is the available RAM left after OS requirements are fulfilled. But how much does an OS requires? That is a very complex question, as RAM is handled dynamically by the OS. Windows 10 as an example can run on as low as 2GB of RAM, but that is not ideal.

Hard drive **read/write speeds** are commonly overlooked. Rather than aiming for a larger hard drive, it is better to get a faster one, especially when you are designing with FPGAs.

## Invest in a nice monitor...

I highly recommend you get a nice big monitor... 27" at least, 2K if you can afford it. Any coder will recommend you a dual monitor setup - for work, I use 2x32" 2K monitors + a 1080p 21" - alas, I have seen people working on a 43"/55" 4K TV (a setup one day I will try) - and I use all of them at the same time, as I do a lot of RTL verification and need to look at waves, compare code, ... but a 27" should suffice.

Again, these days a nice 2K display will last you more than five years - just get a good brand.

## OS - Windows 10/11 vs Ubuntu 20.04 (Linux)

Regarding operating systems, Windows has been always the clear winner for user GUI experience, and available applications for common daily tasks. Linux (and especially Ubuntu or any Linux OS based on Debian) is the winner for development in two categories:

- Open source tools (GTKwave, Python, Verilator, ...)
- Embedded operating system development (FreeRTOS, Embedded Linux, ...)

Without going into any deep argumentation, it is easy to acknowledge this just by looking at Microsoft's growing support for Linux with tools like WSL2 and Visual Code Linux support - which does not mean windows is going anywhere, but that most of the world prefers windows for their majority of tasks, but we need Linux for some special applications/projects.

If you are already with Linux Ubuntu, stay there. For Windows users:

- Some embedded design tools like Arduino, Visual Code or FPGAs (Intel/Altera, AMD/Xilinx) work well under windows and do not have any issues.
- If required, you can use Windows WSL2 or Oracle VirtualBox to have an Ubuntu distro installed.

> Now, regarding Windows 10, upgrade to Windows 11 - if you try the [Microsoft Upgrade assistant](https://www.microsoft.com/en-ca/windows/windows-11) and it complains, create an [installation media](https://www.microsoft.com/en-ca/software-download/windows11) and follow the steps. I have installed Windows 11 using the installation media on machines that did not meet the requirements (e.g. old processor) without any issues. As an example, I installed Windows 11 on a [Microsoft Surface 3](https://support.microsoft.com/en-us/topic/80e52440-0c3a-60e4-b77c-88a5f373ea4d) without any issues, and it works very well (way better than Windows 10 - it came with windows 8.1 originally)
>
> If you have Windows 7, also try to upgrade to Windows 11.

# Embedded Systems R&D

When doing Embedded R&D there are a couple of options for installing the tools/apps and coding your projects:

- A single machine running Windows or Linux (Ubuntu) (or boot doing multiboot)
- Several machines with different OS
- A single powerful machine, with a host OS (Most of the time Windows10/11) and virtual machines running other OS.

## Why several machines?

You can do fine with only Windows 10/11 or Ubuntu. But when you start doing some complex projects or require some tools that are only available for Windows and not Linux, or vice-versa - then you will need multiple machines.

## VMs enter the game

Maintaining several workstations is a pain, plus you need multiple displays/mouse/keyboard or a KVM. With VMs you can install or reinstall OS at your convenience.

### WSL2 vs VirtualBox

When running Windows 10/11 as a host, you have two options to run a Linux distribution:

- <img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Windows_logo_-_2012.svg" alt="WSL2" style="height:1.2em" />**+**<img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png" alt="lINUX" style="height:1.2em" /> WSL2
- <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/virtualbox_logo_icon_169253.png" alt="VirtualBox" style="height:1.2em" /> VirtualBox

Both WSL2 and VirtualBox work as VM. While WSL2 is *"integrated"* into Windows, VirtualBox must be installed and each VM should be created manually.

Most of the time, WSL2 will cover your needs. However, I found that VirtualBox has better support for:

- Installing and re-installing several copies of the same Linux distribution (cloning, copying, snapshots, ...) or running multiple VMs (and pausing them as required)
- USB pass-through (access to USB-UART/JTAG, programming dev. boards, ...)

On the WSL2 side:

- Better GPU access (e.g. CUDA)
- For WSL2 Windows 11 comes with an X11-server integration, which allows you to launch Linux/Ubuntu GUI applications seamlessly. For Windows 10 (if you cannot update to 11), I recommend installing [<img src="https://mobaxterm.mobatek.net/img/moba/xterm_logo.png" alt="https://mobaxterm.mobatek.net/img/moba/xterm_logo.png" style="zoom:40%;" />MobaXterm](https://mobaxterm.mobatek.net/).
- It is possible to install [multiple instances of Ubuntu in WSL2](https://cloudbytes.dev/snippets/how-to-install-multiple-instances-of-ubuntu-in-wsl2), but I have never tried it.
- ❗More stable (I tend to crash a VirtualBox VM more often than a WSL2 session - but maybe it is just me)



> ⚠Unfortunately, you cannot run WSL2 and VirtualBox at the same time[^1]. I have used both, at work I use WSL2 and at home I prefer VirtualBox.
>
> ❗Another option is VMware, which is kind of a VirtualBox (I use VirtualBox for historical issues)

[^1]: Kind off, you can run VirtualBox with WSL2, but it is painfully slow

## Can I use a laptop?

Short answer, yes you can - provided it meets the minimum requirements listed below. Laptops are nice if you travel a lot, or in my case, if you have to take the kids to the dojo every day for a couple of hours - so with a laptop I can blog and R&D there. But laptops are expensive, for the power you eventually will need - a laptop would double the price of a workstation.

So, I have a 17" laptop - and I VPN to my house/work and RDP - and it works great!

# Summary

If you already have a desktop/laptop computer, give it a try first. If you are looking into getting a new one, think about what are you going to do in the long term.

My recommendations for someone that wants to do some embedded projects running on Windows 10/11 or Linux are:

**Native (Windows 10/11, Ubuntu 20.04)** (no VM)

| Item       | Basic Microcontrollers<br />(e.g. Arduino, ESP32, ...) | FPGA(s) / SoC(s)                 | Complex FPGA(s) / AI |
| ---------- | ------------------------------------------------------ | -------------------------------- | -------------------- |
| Processor  | Intel i3 or equivalent (4 cores)                       | Intel i5 or equivalent (4 cores) | Intel i7 (8 cores)   |
| RAM        | 4 GBs                                                  | 8~16GBs                          | 64 GBs               |
| Hard Drive | > 256 GBs<br />SSD is preferable, but SATA6 is OK      | SSD, 512 GBs                     | PCIe, 512GB ~ 1TB    |

**VMs**

If you plan to follow the path of VM, go for an i7 with 64 GBs of RAM. For each VM you will need between 256GB to 512GB of hard drive space.

> 👀 Check my current [HW configuration](({% link _blogs/myhardware.md %}))
