#!/usr/bin/python

import os
import subprocess

home = os.environ["HOME"]

file = open(home+"/scripts/dataRandomWallpaper/cur.cfg", "r")
filename = file.read()
file.close()

print("Name: "+filename)

os.remove(home+"/scripts/dataRandomWallpaper/out/"+filename)

print("change")

subprocess.call(["python", home+"/scripts/randomWallpaper-set.py"])

print("End")
