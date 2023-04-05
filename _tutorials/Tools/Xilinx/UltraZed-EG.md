---

---

# Avnet UltraZed-EG

## [Boards](UltraZed Board Differences)

- AES-ZU3EGES-1-SK-G (red) (Engineering Sample)
- AES-ZU-IOCC-G + XCZU3EG (black)

> ZU3EGES support was removed after Vivado 2017.x - use Avnet.com 

# Getting Started

> [UltraZed-EG element14 Site](https://community.element14.com/products/devtools/avnetboardscommunity/w/boards/23082/ultrazed-eg)

## Base Project on Vivado

### Create Project

1. Create Project

   - Project name: `noarm`
   - Project location: `~/dev/xilinx/vivado/2022.2/ultrazed-eg`
     - [x] Create project subdirectory

2. Project Type

   - [x] RTL Project
     - [x] Do not specify sources at this time

3. Default Part

   - **Boards**

     *Vendor*: avnet.com

     *Name*: Avnet UltraZed-3EG IO Carrier Card

     *Board Rev*: Latest (1.0)

### RTL

1. **IP INTEGRATOR** (Block Design)

   - Create Block Design (default settings)

     1. ➕ Add IP `ctrl + i`

        - zynq $\rightarrow$ `Zynq Ultrascale+ MPSoC`

        - Run Block Automation
          - [x] Apply Board Preset

   - Add Peripherals as AXI-IO blocks

     - Select from Block Design $\rightarrow$ Board
     - For `[DIP switches, LED, Push buttons]`
       - 🖰 Double Left Click
         - ˅ Create new IP $\rightarrow$  ➕ AXI GPIO $\rightarrow$ `GPIO`
       - `Run Connection Automation`  (default 🆗)
     - ⟳ Regenerate Layout
     - 🗹 Validate Design `F6`
     - 💾 Save `ctrl + s`

   - Create HDL Wrapper
     1. Sources $\rightarrow$ Design Sources
     2. 🖰 Right click `design_1`
        - `Create HDL Wrapper...`
        - ⦿ Let Vivado manage wrapper and auto-update
     3. 💾 Save `ctrl + s`

2. **Generate Files**

   1. Generate Bitstream (default 🆗)
      - `Open Implemented Design`
   2. Export Hardware Platform
      - `File` $\rightarrow$ `Export` $\rightarrow$ `Export Hardware...`
      - ⦿ Include bitstream
      - XSA file name: `ultrazed_eg_base.xsa`

### Software

> [Embedded Software Hierarchy in Vitis](https://ohwr.org/project/soc-course/wikis/Embedded-Software-Hierarchy-in-Vitis)

- Launch Vitis

  - Workspace: `${HOME}/dev/xilinx/vitis/2022.2/ultrazed_eg/base/workspace/`

    > One workspace per project is required

- `File` $\rightarrow$ `New > Platform Project` 

  - `Name`: ultrazed_eg

  - Create a new platform from hardware (XSA) $\rightarrow$ `Browse...`

    Load *ultrazed_eg_base.xsa*

  - default 🆗

    - OS: standalone

    - CPU: psu_cortexa53_0

    - Arch: 64-bit

    - Boot Components

      - [x] Generate boot components

        FSBL: ⦿ psu_cortexa53_0

- `File` $\rightarrow$ `New > Application Project` 

  - Select platform: `ultrazed_eg`
  - Application project name: helloWorld
  - Domain: standalone_domain

- `helloworld.c`: source file, modify as required

- 🖰 Right click `helloWorld[standalone_domain]`

  ˃ `Debug As` ˃ `Debug Configurations`

  - `Tab` Main

    - Connection: `New`

      Name: server

      Set as default target

      Host: ###.###.###.### (IP address)

      > Click `Advanced>>` to review connection, as `Test Connection` occasionally fails
      >
      > Click `OK` on save even if `unable to connect` after `Advanced>>` is showing target

  - `Tab` Target Setup

    - [x] Skip Revision Check (for ES target - Red PCB)

  ˃ Build Project

  ˃ `Debug As` ˃ `Launch Hardware (Single Application Debug)`

  > Serial Port Monitor (Teraterm | Putty)
  >
  > Two serial ports, select higher COM @115200



# Troubleshooting

**[Out of the Box UltraZed-EG not working (2017.Jan.30)](https://community.element14.com/products/devtools/avnetboardscommunity/avnetboard-forums/f/ultrazed-hardware-design/37737/out-of-the-box-ultrazed-eg-not-working/137166)**

- IOCC does not come out of reset

> Remove JP1 on SOM (shunt) solved issue

**[Cannot detect Ultrazed Board on host PC using UART and JTAG](https://community.element14.com/products/devtools/avnetboardscommunity/avnetboard-forums/f/ultrazed-hardware-design/36288/cannot-detect-ultrazed-board-on-host-pc-using-uart-and-jtag/204249)**

- Unable to use JTAG SMT2 (micro USB)
- Only working with Xilinx Platform Cable USB II after several POR and USBII plug/unplug

> Apparently there was an issue with the IOCC boards that required several (only if SMT2 gets hot)
>
> An RMA was required for some production boards

> For JTAG connector it is required to set the following jumpers on the IOCC:
>
> - Remove JP1 & ~~JP2~~
>   - JP2 handles SD_WP (SD card write protect HW emulation)
> - Set J1 & J2 to default mode (1-2)
>   - JP1, J1 & J2 manage IDT clock generation
>   - JP1 off, J1[1-2], J2[1-2] is default clocking strategy
>
> [Cannot connect to the Ultrazed board using JTAG](https://community.element14.com/products/devtools/avnetboardscommunity/avnetboard-forums/f/ultrazed-hardware-design/36239/cannot-connect-to-the-ultrazed-board-using-jtag/131003)

## Solution

### ES device (RED board)

To use ES device (RED board), on Vivado Tcl console set

```tcl
set_param xicom.use_bitstream_version_check false
```

### POR

1. Connect PWR to board

2. Connect Platform Cable to board

   > Do NOT connect USB to PC

3. Power up board (switch to ON)
4. Connect USB to PC



# References

| Reference                                                    | Link                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [UltraZed SOM](https://avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/ultrazed/ultrazed-eg/ultrazed-eg-board-family) | https://avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/ultrazed/ultrazed-eg/ultrazed-eg-board-family |
| [AES-ZU-IOCC-G (IO Carrier Card)](https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-zu-iocc-g-3074457345635221598/) | https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-zu-iocc-g-3074457345635221598/ |
| [UltraZed-EG element14 Site](https://community.element14.com/products/devtools/avnetboardscommunity/w/boards/23082/ultrazed-eg) | https://community.element14.com/products/devtools/avnetboardscommunity/w/boards/23082/ultrazed-eg |
| [Digilent JTAG SMT2](https://digilent.com/reference/programmers/jtag-smt2/reference-manual) | https://digilent.com/reference/programmers/jtag-smt2/reference-manual |
| [Embedded Software Hierarchy in Vitis](https://ohwr.org/project/soc-course/wikis/Embedded-Software-Hierarchy-in-Vitis) | https://ohwr.org/project/soc-course/wikis/Embedded-Software-Hierarchy-in-Vitis |

### XDC (IOCC)

```tcl
set_property PACKAGE_PIN W1 [get_ports {gpio_rtl_0_tri_io0]}]
set_property IOSTANDARD LVCMOS18 [get_ports {gpio_rtl_0_tri_io0]}]

set_property IOSTANDARD LVCMOS18 [get_ports D5]
set_property IOSTANDARD LVCMOS18 [get_ports SW1]

set_property PACKAGE_PIN T4 [get_ports D5]
set_property PACKAGE_PIN L2 [get_ports SW1]

set_property PACKAGE_PIN R1 [get_ports SW3]
set_property IOSTANDARD LVCMOS18 [get_ports SW3]
set_property PACKAGE_PIN K2 [get_ports SW2]
set_property IOSTANDARD LVCMOS18 [get_ports SW2]
set_property PACKAGE_PIN U5 [get_ports D6]
set_property IOSTANDARD LVCMOS18 [get_ports D6]
set_property PACKAGE_PIN U6 [get_ports D7]
set_property IOSTANDARD LVCMOS18 [get_ports D7]

set_property PACKAGE_PIN T5 [get_ports {leds3]}]
set_property IOSTANDARD LVCMOS18 [get_ports {leds3]}]
set_property IOSTANDARD LVCMOS18 [get_ports {leds2]}]
set_property IOSTANDARD LVCMOS18 [get_ports {leds1]}]
set_property IOSTANDARD LVCMOS18 [get_ports {leds0]}]
set_property PACKAGE_PIN T7 [get_ports {leds2]}]
set_property PACKAGE_PIN T3 [get_ports {leds1]}]
set_property PACKAGE_PIN U2 [get_ports {leds0]}]
```

