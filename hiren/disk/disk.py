import subprocess
import os
import getpass


def hiren():
    raw_mounted_dir = subprocess.check_output(["volname", "/dev/sr0"])
    hiren = raw_mounted_dir.rstrip().decode("utf-8").lower().replace("_", " ")
    #this will check the name of cd/dvd drive
    dvdurl = ""
    for drive_name in os.listdir("/media/"+getpass.getuser()+"/"):
        if drive_name.lower() == hiren:
            dvdurl = drive_name
            break

    return os.listdir("/media/"+getpass.getuser()+"/"+dvdurl)