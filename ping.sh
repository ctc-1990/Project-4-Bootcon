#!/bin/bash

#Read the output of IP's from Shodan search
cat $1 | while read line
do
ping -c"4" $line
done
