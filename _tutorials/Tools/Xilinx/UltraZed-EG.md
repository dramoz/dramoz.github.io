---

---

# Avnet UltraZed-EG

## [Boards](UltraZed Board Differences)

- AES-ZU3EGES-1-SK-G (red) (Engineering Sample)
- AES-ZU-IOCC-G + XCZU3EG (black)

> ZU3EGES support was removed after Vivado 2017.x - use Avnet.com 

# Getting Started

## Base Project on Vivado



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

# References

| Reference                                                    | Link                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [UltraZed SOM](https://avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/ultrazed/ultrazed-eg/ultrazed-eg-board-family) | https://avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/ultrazed/ultrazed-eg/ultrazed-eg-board-family |
| [AES-ZU-IOCC-G (IO Carrier Card)](https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-zu-iocc-g-3074457345635221598/) | https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-zu-iocc-g-3074457345635221598/ |
| [UltraZed-EG element14 Site](https://community.element14.com/products/devtools/avnetboardscommunity/w/boards/23082/ultrazed-eg) | https://community.element14.com/products/devtools/avnetboardscommunity/w/boards/23082/ultrazed-eg |
| [Digilent JTAG SMT2](https://digilent.com/reference/programmers/jtag-smt2/reference-manual) | https://digilent.com/reference/programmers/jtag-smt2/reference-manual |

