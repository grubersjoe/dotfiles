#!/bin/sh
IMG_URL="https://source.unsplash.com/collection/452289/1920x1200"

wget -O $HOME/.unsplash-wallpaper.jpg $IMG_URL;

dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string:
    var d = desktops();
    for (i=0; i < d.length; i++) {
        d[i].wallpaperPlugin = "org.kde.image";
        d[i].currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
        d[i].writeConfig("Image", "file:///home/joe/.unsplash-wallpaper.jpg");
    }
'
