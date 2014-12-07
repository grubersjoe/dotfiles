#!/usr/bin/env bash

# A simple way to add host specific extra configuration to i3 wm

host_config="hosts/$(hostname).conf"
cd ~/.i3/
cat base.conf > config
sed -i -e '$a\' config
cat $host_config >> config
sed -i -e '$a\' config
i3-msg restart
