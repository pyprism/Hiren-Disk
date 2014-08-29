import subprocess
import os
import getpass
from .models import Box, Disk

#TODO error handling and better response !


def hiren():
    try:
        raw_mounted_dir = subprocess.check_output(["volname", "/dev/sr0"])
    except:
        pass
    if raw_mounted_dir:
        hiren = raw_mounted_dir.rstrip().decode("utf-8").lower().replace("_", " ")
        #this will check the name of cd/dvd drive
        dvdurl = ""
        for drive_name in os.listdir("/media/"+getpass.getuser()+"/"):
            if drive_name.lower() == hiren:
                dvdurl = drive_name
                break

        return os.listdir("/media/"+getpass.getuser()+"/"+dvdurl)


def save_db(disk, box):
    box_obj = Box.objects.filter(box_no=disk)
    if box_obj:
        a = Disk(disk_no=box_obj, serial=disk, contents=content)
        a.save()
    else:
        b = Box(box_no=box)
        b.save()
        xoxo = Box.objects.get(box_no=box)   # need some optimization
        a = Disk(disk_no=xoxo, serial=disk, contents=hiren())
        a.save()