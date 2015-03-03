#!/bin/bash

# (Works only on GNOME based desktops)

WALLPAPER_DIR=$HOME/.wallpaper

cd $WALLPAPER_DIR
while [ 1 ]
do
	set -- *
	length=$#
	random_num=$((( $RANDOM % ($length)) + 1 ))
	gsettings set org.gnome.desktop.background picture-uri "file://$WALLPAPER_DIR/${!random_num}"
	sleep 600 # seconds
done
