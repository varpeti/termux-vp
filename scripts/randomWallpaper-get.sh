#!/bin/bash

home="$HOME"
url="https://alpha.wallhaven.cc/search?q=&categories=111&purity=110&sorting=random&order=desc"
cd "$home/scripts"
mkdir dataRandomWallpaper
cd "$home/scripts/dataRandomWallpaper"
mkdir out

mkdir s
wget -P s/ $url

cd s/
mv ./* "temp1.html"

cat temp1.html | grep -o '<a class="preview" href=['"'"'"][^"'"'"']*alpha.wallhaven.cc[/]wallpaper[^"'"'"']*['"'"'"]' | sed -e 's/^<a class="preview" href=['"'"'"]//' -e 's/["'"'"']$//' >links1.txt

wget -P s/ -i links1.txt

cat s/* | grep -o '<img id="wallpaper" src=['"'"'"][^"'"'"']*[/]full[/][^"'"'"']*['"'"'"]' | sed -e 's/^<img id="wallpaper" src=['"'"'"][/]*//' -e 's/["'"'"']$//' >links2.txt

cd ../

wget -P out/ -N -i s/links2.txt

rm -r s

