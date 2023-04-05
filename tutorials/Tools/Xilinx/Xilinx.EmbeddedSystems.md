# Xilinx Embedded Systems with MPSoC - Oversimplified guide

[TOC]

## Disclaimer

Oversimplified guides are a collection of a bunch of links, tips and guides. I do and use them as a personal fast-track reference guides/tutorials, to condensate and simplify the complexity of R&D in different topics.

My philosophy is to use/link whatever I consider is OK and provide short instructions/guides as required. I update them on a need-basis, so if there is something that requires an update just contact me. Also, it covers only the topics that I have learn on a need/curiosity base.

I am an Electronic Engineer, with FPGA background (as work, most on the verification side now-a-days with Opensource tools) and embedded systems (mostly as a hobby). *"The more you know, the more you realize you don't know.", Aristotle*.

## Preface

This guide float around the following topics:

- [Xilinx MPSoC (ZynQ Ultrascale+)](https://www.xilinx.com/products/silicon-devices/soc/zynq-ultrascale-mpsoc.html) and [Xilinx Tools](https://www.xilinx.com/products/design-tools.html)
- [Ultra96-V2](https://www.avnet.com/wps/portal/us/products/new-product-introductions/npi/aes-ultra96-v2/), [KRIA KV260](https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit.html)
- [Xilinx Tcl](https://www.xilinx.com/content/dam/xilinx/support/documentation/sw_manuals/xilinx2021_2/ug835-vivado-tcl-commands.pdf), [SystemVerilog](https://www.chipverify.com/systemverilog/systemverilog-tutorial)

## Introduction

[Xilinx](https://www.xilinx.com/) is an [FPGA](https://en.wikipedia.org/wiki/Field-programmable_gate_array) (**F**ield **P**rogrammable **G**ate **A**rray) company which is also doing interesting developments with [SoC](https://en.wikipedia.org/wiki/System_on_a_chip) (**S**ystem **O**n a **C**hip) - or what they call now [MPSoC](https://www.xilinx.com/products/silicon-devices/soc/zynq-ultrascale-mpsoc.html) (**M**ulti **P**rocessor **SoC**) and [RFSoC](RFSoC) (**R**adio **F**requency **SoC**). This give focus on **MPSoC** embedded systems implementations, but I think it should work as a guide to the other Xilinx SoC-FPGAs.

With the growing complexity of SoC-FPGAs designs, Xilinx has been introducing new design flows and methodologies which can speed up and improve the design process of embedded systems.

Xilinx has the following tools:

- Software Development Tools
  - Vitis Software Platform
    - Previously SDAccel, SDSoC and SDK (unified in Vitis from 2019.2)
  - Vitis AI
  - Vitis Video Analytics SDK
  - Vitis Accelerated Libraries
  - Vitis Model Composer: toolbox for MATLAB and Simulink for DSP Design
- Hardware Development Tools
  - Vivado ML: [HDL](https://en.wikipedia.org/wiki/Hardware_description_language) (**H**ardware **D**escription **L**anguage) design suite with ML (**M**achine **L**earning) algorithms to improve the design process
    - Design implementation with HDL (text) and IP integrator (Graphic Interface)
      - SystemVerilog, VHDL
    - Design Verification
      - Logic simulation: waveform, debugging tools (break points, ...)
      - Device programming and debug 
    - Design Implementation
  - Vitis Model Composer