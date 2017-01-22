#!/bin/env bash
while [ $# -gt 0 ];do
   if [ $# -gt 1 ];then
     ATTACHMENTS=$ATTACHMENTS,"file://$1"
   else
     ATTACHMENTS="file://$1"$ATTACHMENTS
   fi
   shift
done

thunderbird -compose "attachment='$ATTACHMENTS'"
