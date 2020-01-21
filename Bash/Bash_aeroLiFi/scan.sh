#!/bin/bash

is_alive_ping()
{
	ping $1 -c 1 > /dev/null
	[ $? -eq 0 ] && echo "IP host $1 is up"
}

for i in 192.168.178.{20,37,99}
do
	is_alive_ping $i
done
exit 
