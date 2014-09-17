import subprocess
import os
import getpass
from .models import Box, Disk

#TODO error handling and better response !


def hiren():
    nothing = ""
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

        list_content = os.listdir("/media/"+getpass.getuser()+"/"+dvdurl)
        for i in list_content:  # convert list to simple string ! its not a efficient way ;)
            nothing = nothing + i + ", "
        return nothing


def save_db(box, disk):
    try:
        box_obj = Box.objects.get(box_no=box)
        a = Disk(disk_no=box_obj, serial=disk, contents=hiren())
        a.save()
    except:
        b = Box(box_no=box)
        b.save()
        xoxo = Box.objects.get(box_no=box)   # need some optimization
        hire = Disk(disk_no=xoxo, serial=disk, contents=hiren())
        hire.save()