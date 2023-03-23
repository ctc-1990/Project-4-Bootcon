#!/bin/bash

#Read list of IP's from Shodan search
cat $1 | while read line
#Perform nmap scan on list
do
nmap -sS -F $line
done
