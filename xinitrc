#!/bin/sh

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

# Keymap manipulations
if [ -s ~/.xmodmap ]; then
    xmodmap ~/.xmodmap
fi

# Extra key bindings
if [ -s ~/.xbindkeysrc ]; then
	xbindkeys
fi

~/.i3/make-config.sh
exec i3
