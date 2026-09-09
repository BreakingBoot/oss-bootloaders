# Open-Source Bootloaders

## Overview

The bootloader corpus behind [BootBench](https://github.com/BreakingBoot/BootBench),
the dataset for *SoK: All You Ever Wanted to Know About Bootloader Security but
Were Afraid to Ask* (Glosner and Machiry, IEEE S&P 2026).

Every bootloader is a git submodule pinned to an upstream commit, grouped by
type. Nothing is vendored: this repository stores pointers, so a given revision
of the corpus is reproducible without carrying tens of gigabytes of third-party
history.

```bash
git clone --recurse-submodules https://github.com/BreakingBoot/oss-bootloaders.git
git submodule update --init type1/edk2       # or just the one you need
```

Bootloaders are classified by how they initialise the machine and how they hand
off. The table at the end of this file is generated from the submodules
themselves by `tools/generate_table.py` in the BootBench superproject.

## Type 1

**Firmware bootloaders.** Boot from hardware and present a hardware-agnostic
interface to whatever runs next, optionally loading another bootloader or a
standalone application. They run immediately after the hardware root of trust
hands off to software, bring up the silicon, then expose a stable interface --
UEFI system tables and Boot Services, or the legacy BIOS interrupt interface.
Being OS-agnostic, they do not prepare an operating system themselves.

coreboot, EDK-II, SeaBIOS, Slim Bootloader, OpenBIOS, Open Firmware, Hostboot,
Libreboot, oreboot, Project Mu, OpenSBI.

## Type 2

**OS bootloaders.** Boot from an already-initialised system and prepare for an
operating system or hypervisor. Their job is to locate a kernel, load it, and
transfer control with the right arguments and tables, which makes them
configuration-driven and chainloadable in a way Type 1 is not.

GRUB, shim, systemd-boot, Limine, rEFInd, iPXE, Depthcharge, Little Kernel,
lk2nd, Skiboot, OpenCore, Clover, tboot, u-root, petitboot, kexec-tools,
SYSLINUX, BOOTBOOT.

## Type 3

**Monolithic bootloaders.** Combine the jobs of Type 1 and Type 2, booting
directly from hardware into an operating system with no handoff between stages.
Smaller and faster, but tightly coupled to the board. The norm for IoT devices
and microcontrollers.

U-Boot, Barebox, MCUboot, ARM Trusted Firmware, Trusted Firmware-M, wolfBoot,
rustBoot, OpenBLT, RedBoot, Optiboot, Katapult, and the vendor bootloaders for
nRF52, STM32 and Mbed.

Types 1 and 2 chained together are *staged booting*, typical of desktops,
servers and phones. Type 3 is *monolithic booting*.

## Dataset

This corpus is one of three repositories:

| Repository | Holds |
|---|---|
| [oss-bootloaders](https://github.com/BreakingBoot/oss-bootloaders) | the bootloader source trees (this repository) |
| [bootloader_cve_db](https://github.com/BreakingBoot/bootloader_cve_db) | CVEs mined from the CVE Project records, classified by type |
| [bootloader_vuln_commits](https://github.com/BreakingBoot/bootloader_vuln_commits) | vulnerability-fixing commits mined from these histories |

The commit-mining stage reads the histories here, so a bootloader added to this
repository is not represented in the vulnerability data until that runs again.
There is no CI: the update scripts live in the
[BootBench](https://github.com/BreakingBoot/BootBench) superproject under
`scripts/`.

| Type | Bootloader | Commits | First Commit | Latest Commit |
|------|-----------|---------|--------------|---------------|
| Type 1 - Firmware | [LakeBIOS](https://github.com/AtieP/LakeBIOS) | 112 | 2021-06-20 | 2021-09-22 |
| Type 1 - Firmware | [coreboot](https://github.com/coreboot/coreboot) | 64923 | 2003-04-15 | 2026-09-09 |
| Type 1 - Firmware | [edk2](https://github.com/tianocore/edk2) | 33529 | 2006-04-21 | 2024-11-17 |
| Type 1 - Firmware | [edk2-platforms](https://github.com/tianocore/edk2-platforms) | 4858 | 2017-08-03 | 2026-09-02 |
| Type 1 - Firmware | [firmware-open](https://github.com/system76/firmware-open) | 960 | 2019-03-18 | 2026-08-24 |
| Type 1 - Firmware | [hostboot](https://github.com/open-power/hostboot) | 25463 | 2010-05-13 | 2026-04-28 |
| Type 1 - Firmware | [lbmk](https://codeberg.org/libreboot/lbmk) | 4126 | 2021-05-18 | 2026-09-07 |
| Type 1 - Firmware | [mu_basecore](https://github.com/microsoft/mu_basecore) | 35809 | 2006-04-21 | 2026-09-04 |
| Type 1 - Firmware | [openbios](https://github.com/openbios/openbios) | 1636 | 2006-04-26 | 2026-07-04 |
| Type 1 - Firmware | [openfirmware](https://github.com/MitchBradley/openfirmware) | 3861 | 2006-11-13 | 2022-04-26 |
| Type 1 - Firmware | [opensbi](https://github.com/riscv-software-src/opensbi) | 2225 | 2018-12-11 | 2026-09-05 |
| Type 1 - Firmware | [oreboot](https://github.com/oreboot/oreboot) | 29214 | 2003-04-15 | 2026-07-13 |
| Type 1 - Firmware | [seabios](https://github.com/coreboot/seabios) | 2699 | 2008-02-25 | 2024-10-25 |
| Type 1 - Firmware | [slimbootloader](https://github.com/slimbootloader/slimbootloader) | 2169 | 2018-09-13 | 2025-04-09 |
| | | | | |
| Type 2 - OS | [CloverBootloader](https://github.com/CloverHackyColor/CloverBootloader) | 2161 | 2019-09-02 | 2024-11-09 |
| Type 2 - OS | [MiniVisorPkg](https://github.com/tandasat/MiniVisorPkg) | 38 | 2020-02-22 | 2024-08-15 |
| Type 2 - OS | [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) | 4922 | 2018-10-02 | 2025-04-09 |
| Type 2 - OS | [aboot](https://github.com/mattst88/aboot) | 130 | 2001-10-08 | 2021-08-01 |
| Type 2 - OS | [bootboot](https://gitlab.com/bztsrc/bootboot) | 356 | 2018-06-05 | 2026-03-15 |
| Type 2 - OS | [bootloader](https://github.com/rust-osdev/bootloader) | 1323 | 2017-12-14 | 2025-08-01 |
| Type 2 - OS | [chameleon](https://github.com/rescbr/chameleon) | 1235 | 2010-01-14 | 2018-01-14 |
| Type 2 - OS | [depthcharge](https://chromium.googlesource.com/chromiumos/platform/depthcharge/) | 4528 | 2012-08-31 | 2025-04-10 |
| Type 2 - OS | [easyboot](https://gitlab.com/bztsrc/easyboot) | 66 | 2023-10-28 | 2024-10-20 |
| Type 2 - OS | [grub](https://git.savannah.gnu.org/git/grub) | 10996 | 2002-12-27 | 2024-10-31 |
| Type 2 - OS | [ipxe](https://github.com/ipxe/ipxe) | 6805 | 2005-03-08 | 2024-10-29 |
| Type 2 - OS | [kexec-tools](https://github.com/horms/kexec-tools) | 1451 | 2006-07-27 | 2026-08-24 |
| Type 2 - OS | [limine](https://github.com/limine-bootloader/limine) | 2811 | 2019-05-15 | 2024-11-15 |
| Type 2 - OS | [linuxboot](https://github.com/linuxboot/linuxboot) | 1045 | 2016-07-25 | 2024-12-03 |
| Type 2 - OS | [lk](https://github.com/littlekernel/lk) | 2701 | 2008-09-01 | 2025-04-11 |
| Type 2 - OS | [lk2nd](https://github.com/msm8916-mainline/lk2nd) | 8952 | 2005-06-08 | 2025-04-06 |
| Type 2 - OS | [petitboot](https://github.com/open-power/petitboot) | 1520 | 2007-04-02 | 2026-01-12 |
| Type 2 - OS | [quibble](https://github.com/maharmstone/quibble) | 371 | 2020-02-13 | 2024-06-23 |
| Type 2 - OS | [refind](https://git.code.sf.net/p/refind/code) | 887 | 2012-03-25 | 2024-12-05 |
| Type 2 - OS | [shim](https://github.com/rhboot/shim) | 1143 | 2012-04-11 | 2024-11-12 |
| Type 2 - OS | [skiboot](https://github.com/open-power/skiboot) | 5738 | 2014-07-02 | 2025-04-04 |
| Type 2 - OS | [syslinux](https://repo.or.cz/syslinux) | 7317 | 1998-01-31 | 2019-02-20 |
| Type 2 - OS | [systemd](https://github.com/systemd/systemd) | 80703 | 2005-04-26 | 2025-04-11 |
| Type 2 - OS | [tboot-mirror](https://github.com/BreakingBoot/tboot-mirror) | 697 | 2007-10-25 | 2025-04-11 |
| Type 2 - OS | [tosaithe](https://github.com/davmac314/tosaithe) | 187 | 2021-07-24 | 2024-09-28 |
| Type 2 - OS | [u-root](https://github.com/u-root/u-root) | 5690 | 2012-10-29 | 2026-09-08 |
| Type 2 - OS | [x86-bootloader](https://github.com/lukearend/x86-bootloader) | 23 | 2021-10-09 | 2022-07-24 |
| | | | | |
| Type 3 - Monolithic | [Adafruit_nRF52_Bootloader](https://github.com/adafruit/Adafruit_nRF52_Bootloader) | 1027 | 2018-01-25 | 2026-05-21 |
| Type 3 - Monolithic | [IMBootloader](https://github.com/IMProject/IMBootloader) | 101 | 2021-04-28 | 2024-03-28 |
| Type 3 - Monolithic | [STM32duino-bootloader](https://github.com/rogerclarkmelbourne/STM32duino-bootloader) | 145 | 2015-05-16 | 2020-03-10 |
| Type 3 - Monolithic | [arduino-variometer](https://github.com/prunkdump/arduino-variometer) | 163 | 2016-09-20 | 2019-12-17 |
| Type 3 - Monolithic | [arm-trusted-firmware](https://github.com/ARM-software/arm-trusted-firmware) | 15691 | 2013-10-25 | 2024-11-19 |
| Type 3 - Monolithic | [barebox](https://github.com/barebox/barebox) | 27915 | 2000-06-17 | 2025-04-09 |
| Type 3 - Monolithic | [bootloader](https://github.com/wookey-project/bootloader) | 133 | 2018-09-24 | 2021-08-31 |
| Type 3 - Monolithic | [firmware](https://github.com/meshtastic/firmware) | 9455 | 2020-02-01 | 2025-04-17 |
| Type 3 - Monolithic | [harmony](https://github.com/Microchip-MPLAB-Harmony/bootloader) | 489 | 2018-07-17 | 2025-07-01 |
| Type 3 - Monolithic | [katapult](https://github.com/Arksine/katapult) | 246 | 2021-01-23 | 2026-03-20 |
| Type 3 - Monolithic | [mbed-bootloader](https://github.com/PelionIoT/mbed-bootloader) | 66 | 2018-03-23 | 2020-08-26 |
| Type 3 - Monolithic | [mcuboot](https://github.com/mcu-tools/mcuboot) | 2420 | 2016-12-12 | 2024-11-19 |
| Type 3 - Monolithic | [openblt](https://github.com/feaser/openblt) | 662 | 2011-11-10 | 2024-09-16 |
| Type 3 - Monolithic | [optiboot](https://github.com/Optiboot/optiboot) | 293 | 2010-04-03 | 2026-02-14 |
| Type 3 - Monolithic | [redboot](https://github.com/hharte/ecos) | 2923 | 1999-05-11 | 2023-11-12 |
| Type 3 - Monolithic | [rustBoot](https://github.com/nihalpasham/rustBoot) | 281 | 2021-07-25 | 2024-09-11 |
| Type 3 - Monolithic | [stm32-mw-openbl](https://github.com/STMicroelectronics/stm32-mw-openbl) | 8 | 2021-10-18 | 2025-06-05 |
| Type 3 - Monolithic | [tock-bootloader](https://github.com/tock/tock-bootloader) | 176 | 2017-03-08 | 2024-02-07 |
| Type 3 - Monolithic | [trusted-firmware-m](https://github.com/TrustedFirmware-M/trusted-firmware-m) | 8683 | 2017-11-30 | 2026-09-07 |
| Type 3 - Monolithic | [u-boot](https://github.com/u-boot/u-boot) | 98975 | 2000-06-17 | 2025-04-10 |
| Type 3 - Monolithic | [wolfBoot](https://github.com/wolfSSL/wolfBoot) | 2067 | 2018-10-10 | 2025-03-28 |
