# Bootloader Collection  

This repository aggregates a wide variety of bootloaders, organized by type.  
Each bootloader is included as a git submodule and linked to its upstream repository.  

---

## Type 1 Bootloaders (Firmware / Early Boot)  
- [LakeBIOS](https://github.com/AtieP/LakeBIOS)  
- [EDK2](https://github.com/tianocore/edk2)  
- [OpenBIOS](https://github.com/openbios/openbios)  
- [SeaBIOS](https://github.com/coreboot/seabios)  
- [Slim Bootloader](https://github.com/slimbootloader/slimbootloader)  
- [coreboot](https://github.com/coreboot/coreboot)  
- [OpenFirmware](https://github.com/MitchBradley/openfirmware)  
- [Firmware-Open (System76)](https://github.com/system76/firmware-open)  
- [Hostboot (OpenPOWER)](https://github.com/open-power/hostboot)  
- [Libreboot (lbmk)](https://codeberg.org/libreboot/lbmk)  

---

## Type 2 Bootloaders (OS / Hypervisor Loaders)  
- [EasyBoot](https://gitlab.com/bztsrc/easyboot)  
- [Tosaithe](https://github.com/davmac314/tosaithe)  
- [GRUB](https://git.savannah.gnu.org/git/grub.git)  
- [CloverBootloader](https://github.com/CloverHackyColor/CloverBootloader)  
- [Limine](https://github.com/limine-bootloader/limine)  
- [Chameleon](https://github.com/rescbr/chameleon)  
- [Shim](https://github.com/rhboot/shim)  
- [Open-iSCSI](https://github.com/open-iscsi/open-iscsi)  
- [iPXE](https://github.com/ipxe/ipxe)  
- [MiniVisorPkg](https://github.com/tandasat/MiniVisorPkg)  
- [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg)  
- [lk2nd](https://github.com/msm8916-mainline/lk2nd)  
- [Skiboot (OpenPOWER)](https://github.com/open-power/skiboot)  
- [Depthcharge (ChromeOS)](https://chromium.googlesource.com/chromiumos/platform/depthcharge/)  
- [Little Kernel (lk)](https://github.com/littlekernel/lk)  
- [rEFInd](https://git.code.sf.net/p/refind/code)  
- [systemd-boot](https://github.com/systemd/systemd)  
- [tboot](https://github.com/BreakingBoot/tboot-mirror)  
- [aboot](https://github.com/mattst88/aboot)  
- [LinuxBoot](https://github.com/linuxboot/linuxboot)  
- [Quibble](https://github.com/maharmstone/quibble)  
- [Rust Bootloader](https://github.com/rust-osdev/bootloader)  
- [x86-bootloader](https://github.com/lukearend/x86-bootloader)  

---

## Type 3 Bootloaders (Embedded / Microcontroller / SoC)  
- [Arduino Variometer Bootloader](https://github.com/prunkdump/arduino-variometer)  
- [OpenBLT](https://github.com/feaser/openblt)  
- [MCUboot](https://github.com/mcu-tools/mcuboot)  
- [IMBootloader](https://github.com/IMProject/IMBootloader)  
- [ARM Trusted Firmware](https://github.com/ARM-software/arm-trusted-firmware)  
- [U-Boot](https://github.com/u-boot/u-boot)  
- [Barebox](https://github.com/barebox/barebox)  
- [wolfBoot](https://github.com/wolfSSL/wolfBoot)  
- [RedBoot (ecos)](https://github.com/hharte/ecos)  
- [Meshtastic Firmware](https://github.com/meshtastic/firmware)  
- [Wookey Bootloader](https://github.com/wookey-project/bootloader)  
- [rustBoot](https://github.com/nihalpasham/rustBoot)  
- [STM32 OpenBL](https://github.com/STMicroelectronics/stm32-mw-openbl)  
- [Harmony Bootloader (Microchip)](https://github.com/Microchip-MPLAB-Harmony/bootloader)  

---

## Cloning with Submodules  

To clone this repository and initialize all bootloader submodules:  

```bash
git clone --recursive <this-repo-url>
