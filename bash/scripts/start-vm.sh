#!/usr/bin/env bash

# A simple shorthand to start a specific VM image

modules=( "vboxdrv" "vboxnetflt" "vboxnetadp" )

declare -A vms
vms=( [ie8]="cff5fc40-876e-428c-9875-106e96a61a3d" 
	  [ie9]="79fd83c3-23b8-443a-adb0-1cd16acd1549" 
	  [ie10]="2e43754f-350a-48da-b7e2-46219ab20da6" 
	  [ie11]="4d816a3e-215a-4d70-bf6a-6a8ca6dcf5f4" )

if [ -z "$1" ]; then
    echo "Argument VM id missing!"
    exit 1
fi

for i in "${modules[@]}"; do
	if ! lsmod | grep "$i" &> /dev/null ; then
		sudo modprobe "$i"
	fi
done

for i in "${vms[@]}"; do
	if [[ ${vms[$1]} ]]; then
		echo "Starting "$1"..."
		virtualbox --startvm ${vms[$1]}
		break
	fi
done
