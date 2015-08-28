#!/usr/bin/env bash

# A simple way to add host specific extra configuration to i3 wm

function insert_newline {
    counter=${1:-1} # counter = $1 || 1
    while [  $counter -gt 0 ]; do
        echo >> config # (no check if a newline is already present)
        let counter=counter-1 
    done    
}

host_config="hosts/$(hostname).conf"
cd ~/.i3/
cat base.conf > config
insert_newline 2
echo "## Host specific config for $(hostname)" >> config
insert_newline
cat $host_config >> config
insert_newline
i3-msg restart
