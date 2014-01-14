from commands import getoutput

rawMountedDir = getoutput("lsblk -o MOUNTPOINT")

mountDir = ""

 (?<=prism/).*?(?<=\\)