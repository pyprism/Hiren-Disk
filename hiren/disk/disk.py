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
    print(raw_mounted_dir.strip().decode('utf-8').replace("_", " "))
    hiren = raw_mounted_dir.strip().decode('utf-8').replace("_", "\ ") + "/"
    print(hiren)
    os.chdir("/media/" + getpass.getuser() + "/" + hiren)
    #os.chdir("/media/" + getpass.getuser() + "/" + raw_mounted_dir.strip().decode('utf-8').replace("_", " ") + "/")
    #a = subprocess.check_output(["ls", "/media/" + getpass.getuser() + "/" + raw_mounted_dir.strip().decode('utf-8').replace("_", "\ ") + "/"])
    #print(a.decode('utf-8'))
    #return os.listdir(os.getcwd())

hiren()