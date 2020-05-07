###########################################################################################
# Copyright (c), 2020 - Analog Devices Inc. All Rights Reserved. 
# This software is PROPRIETARY & CONFIDENTIAL to Analog Devices, Inc.
# and its licensors.
###########################################################################################
# File:
#   <config.py>
# Description:
#   Provide necessary configuration macros used in this tool, users can edit this when use
#
###########################################################################################

# OPTIONS varaiables
MACHINE = 'adsp-sc584-ezkit'
EMULATOR = '2000'
BOOTTYPE = 'nfsboot'
COM_PORT = '/dev/ttyUSB0'
DHCP = False
SERVER_IP = '10.100.4.174'
IP_ADDR = '10.100.4.50'
UBOOT_UPDATE = True
DEPLOY_FOLDER = ''

# BOOT commands for different boot type
DHCP_CMD = ['dhcp']
SET_IP = ['set serverip SERVER_IP', 'set ipaddr IP_ADDR']
BOOT_CMD = {
'update_uboot': ['run update'],
'nfsboot': ['run nfsboot'],
'ramboot': ['run ramboot'],
'sdcardboot': ['run sdcardboot']
}

# Serial port information
SERIAL_BAUDRATE= 57600
SERIAL_TIMEOUT = 1

# verify pass message
UBOOT_LOAD_PASS_MSG = 'sc #'
KERNEL_LOAD_PASS_MSG = 'MACHINE login:'

# TIMEOUT value for load
SHORT_SLEEP_TIME = 2
WAIT_TIMEOUT = 5
UART_TIMEOUT = 3*60

# OpenOCD related parameters
OPENOCD_HOME = '/opt/analog/cces/2.9.2' # TODO this need change when we have openOCD repo
OPENOCD_CONFIG_PATH = 'ARM/openocd/share/openocd/scripts/'
OPENOCD_PATH = 'ARM/openocd/bin/'
OPENOCD_DEFAULT_BINARY = 'openocd'
OPENOCD_TARGET_CFG_FILE = {
    'sc58[4|9]':'adspsc58x.cfg',
    'sc573':'adspsc57x.cfg',
}

# GDB related parameters
GDB_OPENOCD_DEFAULT_PORT = '3333'
GDB_DEFAULT_PATH = 'ARM/arm-none-eabi/bin/'
GDB_DEFAULT_BINARY = 'arm-none-eabi-gdb'
GDB_LOAD_UBOOT = 'u-boot'
GDB_ELF_FILE = 'init.elf'
GDB_ERROR_CMD = r'\^error,msg=(\".*\")'
GDB_PROMPT = '(gdb) \n'
GDB_SEND_CMDS = ['load %s'%GDB_ELF_FILE, 'c', 'Ctrl-c', 'load %s' %GDB_LOAD_UBOOT, 'c']

# utility related parameters when do image copy
IMAGE_TYPES = ['adsp-sc5xx-full', 'adsp-sc5xx-minimal', 'adsp-sc5xx-ramdisk'] 
COPY_DST_FOLDER = '/tftpboot'
NFS_TAR_FILE_POSTFIX = '.tar.xz'
NFS_DST_FOLDER= '/romfs'
NFS_CP_CMD_LIST = ["sudo rm -rf NFSFOLDER", "sudo mkdir NFSFOLDER", "sudo chmod 777 NFSFOLDER", "tar -xvf NFS_SRC_TAR_FILE -C NFSFOLDER" ]
RAMDISK_FILE_POSTFIX = '.cpio.xz.u-boot'
RAMDISK_FILE_NAME = 'ramdisk.cpio.xz.u-boot'
UBOOT_FILE_LIST = ['u-boot', 'u-boot.ldr']
Z_IMAGE = 'zImage'
DTB_POSTFIX = '.dtb'