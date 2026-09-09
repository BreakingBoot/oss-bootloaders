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

