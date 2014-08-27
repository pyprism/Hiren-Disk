import subprocess
import os
import getpass
from .models import Box, Disk

#TODO error handling and better response !


def hiren(disk, box):
    try:
        raw_mounted_dir = subprocess.check_output(["volname", "/dev/sr0"])
    except:
        pass
    hiren = raw_mounted_dir.rstrip().decode("utf-8").lower().replace("_", " ")
    #this will check the name of cd/dvd drive
    dvdurl = ""
    for drive_name in os.listdir("/media/"+getpass.getuser()+"/"):
        if drive_name.lower() == hiren:
            dvdurl = drive_name
            break

    content = os.listdir("/media/"+getpass.getuser()+"/"+dvdurl)
    b = Box(disk_no=box)
    b.save()
    a = Disk(serial=disk, title=content)
    a.save()
    print("x")