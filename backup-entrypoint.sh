#!/bin/sh

# sleep 1234567890

pip3 install --upgrade --no-cache-dir boto3
if [ "$1" == "restore" ]
then
    restore
else
    echo starting cron daemon
    crond -l 2 -f
    # NOTE: this was usefull
    # src: https://gist.github.com/andyshinn/3ae01fa13cb64c9d36e7#file-dockerfile
fi
