#!/bin/sh

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

# Keymap manipulations
if [ -s ~/.Xmodmap ]; then
    xmodmap ~/.Xmodmap
fi

~/.i3/build.py
exec i3
