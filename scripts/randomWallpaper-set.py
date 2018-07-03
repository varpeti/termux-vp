#!/usr/bin/python

import os
import random
import subprocess

home = os.environ["HOME"]

filename = random.choice(os.listdir(home+"/scripts/dataRandomWallpaper/out"))

print("Name: "+filename)

file = open(home+"/scripts/dataRandomWallpaper/cur.cfg", "w")
file.write(filename)
file.close()

subprocess.call(["termux-wallpaper", "-f", home+"/scripts/dataRandomWallpaper/out/"+filename])

print("End")