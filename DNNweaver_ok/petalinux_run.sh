#this shell can generate BOOT.BIN and uImage to build petalinux platform for zedboard

# what you have to do is to change petalinuxv3 to whatever is named by yourself

#petalinux/settings.sh and vivado"s settings64.sh is available
#built in../usr/software

#!/bin/bash
source /workspace/home/liumin/software/petalinux/settings.sh

#BSP installation
#cd /workspace/.#directory under which you want Petalinux projects to be created
#petalinux-create -t project -s <path-to-bsp>

source /workspace/home/liumin/software/vivado14.4/Vivado/2014.4/settings64.sh
cd  /workspace/home/zhoucc/software
petalinux-create --type project --template zynq --name petalinuxv3 #petalinuxv2 is the folder defined by yourself
cd /workspace/home/zhoucc/software/petalinuxv3 #petalinuxv2 is the folder defined by yourself
petalinux-config --get-hw-description=/workspace/home/zhoucc

petalinux-build

petalinux-package --image -c kernel --format uImage

petalinux-package --boot --fsbl /workspace/home/zhoucc/software/petalinuxv3/images/linux/zynq_fsbl.elf --fpga  /workspace/home/zhoucc/software/petalinuxv3/images/linux/first_zynq_system_wrapper.bit --u-boot /workspace/home/zhoucc/software/petalinuxv3/images/linux/u-boot.elf #reference to guide v17.1

petalinux-package --prebuilt --fpga /workspace/home/zhoucc/software/petalinuxv3/images/linux/first_zynq_system_wrapper.bit


