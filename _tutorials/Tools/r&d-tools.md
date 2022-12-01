---

---

[TOC]

---

## RISC-V

### Requirements

- Ubuntu >20.04 (OS or Win+WSL2)
- Python >3.8.10

### Toolchain (gcc/gdb)

```bash
# Install
cd /data/tools/
wget https://static.dev.sifive.com/dev-tools/freedom-tools/v2020.12/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
tar -xvzf riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
rm -f riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
mv riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14 riscv64-unknown-elf-toolchain

# Test
cd riscv64-unknown-elf-toolchain/bin/

riscv64-unknown-elf-gcc --version
> riscv64-unknown-elf-gcc (SiFive GCC-Metal 10.2.0-2020.12.8) 10.2.0
> Copyright (C) 2020 Free Software Foundation, Inc.
> This is free software; see the source for copying conditions.  There is NO
> warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

### HEX to Verilog

```bash
# Clone repository elf2hex
mkdir -p ~/repos; cd ~/repos
git clone git@github.com:sifive/elf2hex.git

# Install
cd elf2hex
autoreconf -i
./configure --target=riscv64-unknown-elf --prefix /data/tools/riscv64-unknown-elf-toolchain
make -j $(nproc)
sudo make install

# Test
cd /data/tools/riscv64-unknown-elf-toolchain/bin/
./riscv64-unknown-elf-elf2hex --help
> ./riscv64-unknown-elf-elf2hex [-h, --help] --bit-width BIT_WIDTH --input INPUT.ELF [--output OUTPUT.HEX]
```

### JTAG Debugging (OpenOCD-VexRiscv)

```bash
# Dependencies
sudo apt install libtool automake libusb-1.0-0-dev texinfo libusb-dev libyaml-dev pkg-config

# Install
mkdir -p ~/repos; cd ~/repos
git clone https://github.com/SpinalHDL/openocd_riscv
cd openocd_riscv
./bootstrap
./configure --prefix=/data/tools/openocd --enable-ftdi --enable-dummy
make -j $(nproc)
sudo make install

# Test
openocd --version
> Open On-Chip Debugger 0.11.0+dev-02578-g50f74cd37-dirty (2022-10-13-10:28)
>Licensed under GNU GPL v2
>For bug reports, read
>        http://openocd.org/doc/doxygen/bugs.html
```

## Verilator

```bash
# Prerequisites:
#sudo apt-get install git perl python3 make autoconf g++ flex bison ccache
#sudo apt-get install libgoogle-perftools-dev numactl perl-doc
#sudo apt-get install libfl2  # Ubuntu only (ignore if gives error)
#sudo apt-get install libfl-dev  # Ubuntu only (ignore if gives error)
#sudo apt-get install zlibc zlib1g zlib1g-dev  # Ubuntu only (ignore if gives error)

git clone https://github.com/verilator/verilator   # Only first time

# Every time you need to build:
unset VERILATOR_ROOT  # For bash
cd verilator
git pull         # Make sure git repository is up-to-date
git tag          # See what versions exist
#git checkout master      # Use development branch (e.g. recent bug fixes)
#git checkout stable      # Use most recent stable release
#git checkout v{version}  # Switch to specified release version

autoconf
./configure
make -j $(nproc)
sudo make install
```