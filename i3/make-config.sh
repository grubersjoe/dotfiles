#!/usr/bin/env bash

# A simple way to add host specific extra configuration to i3 wm

host=$(hostname)
host_config="hosts/$(hostname).conf"
cd ~/.i3/
cat base.conf > config
cat $host_config >> config
i3-msg reload > /dev/null
