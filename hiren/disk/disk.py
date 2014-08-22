# from commands import getoutput
#
# from os import chdir , listdir , getcwd
#
# from getpass import getuser
#
#
# def hiren():
# 	rawMountedDir = getoutput("volname /dev/sr0")
# 	while True:
# 		if rawMountedDir == "volname: No medium found" :
# 			rawMountedDir = getoutput("volname /dev/sr0")
# 		elif rawMountedDir == "volname: Input/output error":
# 			rawMountedDir = getoutput("volname /dev/sr0")
# 		else:
# 			break
# 	chdir("/media/" + getuser() + "/" + rawMountedDir.rstrip() + "/")
# 	return listdir(getcwd())

import subprocess
import os
import getpass


def hiren():
    raw_mounted_dir = subprocess.check_output(["volname", "/dev/sr0"])
    while True:
        if raw_mounted_dir == "volname: No medium found":
            raw_mounted_dir = subprocess.check_output(["volname /dev/sr0"])
        elif raw_mounted_dir == "volname: Input/output error":
            raw_mounted_dir = subprocess.check_output(["volname /dev/sr0"])
        else:
            break
    hiren =raw_mounted_dir.rstrip().decode("utf-8").lower()
    #this will check the name of cd/dvd drive
    dvdurl=""
    for drive_name in os.listdir("/media/"+getpass.getuser()+"/"):
        if drive_name.lower()==hiren:
            dvdurl=drive_name
            break

    os.chdir("/media/"+getpass.getuser()+"/"+dvdurl)
"""
    #walking through the mounted devices this is real naive :P
    for root, dirs, files in os.walk("/media/"+getpass.getuser()+"/"):
        if hiren ==root.lower():
            dvdurl=root
            break
        print("Searching roots: ",root)
    print(dvdurl)
    #os.chdir("/media/" + getpass.getuser() + "/" + raw_mounted_dir.strip().decode('utf-8').replace("_", " ") + "/")
    #a = subprocess.check_output(["ls", "/media/" + getpass.getuser() + "/" + raw_mounted_dir.strip().decode('utf-8').replace("_", "\ ") + "/"])
    #print(a.decode('utf-8'))
    #return os.listdir(os.getcwd())
"""
hiren()