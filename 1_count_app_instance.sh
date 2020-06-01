#!/bin/bash

##  Assume the list of hostnames is in a file called 'hostnames.txt'
##  Assume SSH auth established and the pri key is ssh-key.pri
##  Assume SSH user is called 'user'


# what if appXXXX (where X=[0-9]) is acceptable but not appYYYY (where Y=[a-z,A-Z])

HostnamesList="/path/to/hostnames.txt"
SSHKey="/path/to/ssh-key.pri"
SSHUser="user"
cmd="ps -aux | grep -x app | wc -l"

for host in $(cat $HostnamesList); do
  count=`ssh -i $SSHKey $SSHUser@$host $cmd`
  if [ $count -ne 4 ]; then
    echo "$host: Unhealthy"
  fi
done
