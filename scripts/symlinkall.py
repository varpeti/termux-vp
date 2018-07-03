#!/usr/bin/python

import os
import shutil
import re

home = os.environ["HOME"]

print("clear")

shutil.rmtree(home+"/.shortcuts", ignore_errors=True)
os.mkdir(home+"/.shortcuts")
shutil.rmtree(home+"/.termux/tasker", ignore_errors=True)
os.mkdir(home+"/.termux/tasker")


print("copy")

file = open(home+"/scripts/symlink.cfg", "r")
for line in file:
    so = re.match("^(.+) ([0-1]+) ([0-1]+)$",line)
    if so:
        print(so.group(1)+" | "+so.group(2)+" | "+so.group(3))
        os.chmod(home+"/scripts/"+so.group(1), 0o700)
        if so.group(2) == "1":
            os.symlink(home+"/scripts/"+so.group(1),home+"/.shortcuts/"+so.group(1))
        if so.group(3) == "1":
            os.symlink(home+"/scripts/"+so.group(1),home+"/.termux/tasker/"+so.group(1))

file.close()

print("end")