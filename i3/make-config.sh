#!/usr/bin/env bash

# A simple way to add distribution specific extra configuration to i3 wm
# (lsb_release needs to be installed)

distro=$(lsb_release -is)
extra_config="${distro,,}.conf"
cd ~/.i3/
cat base.conf > config
cat $extra_config >> config
i3-msg reload > /dev/null
