from commands import getoutput

from os import chdir , listdir , getcwd

from getpass import getuser

def hiren():
	rawMountedDir = getoutput("volname /dev/sr0")
	while True:
		if rawMountedDir == "volname: No medium found" :
			rawMountedDir = getoutput("volname /dev/sr0")
		elif rawMountedDir == "volname: Input/output error":
			rawMountedDir = getoutput("volname /dev/sr0")
		else:
			break
	chdir("/media/" + getuser() + "/" + rawMountedDir.rstrip() + "/")
	return listdir(getcwd())