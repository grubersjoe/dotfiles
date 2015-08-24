#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

# GNOME keyring
# eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets)
# export SSH_AUTH_SOCK

# Extra keybindings
if [ -s ~/.xmodmap ]; then
    xmodmap ~/.xmodmap
fi

~/.i3/make-config.sh
exec i3
