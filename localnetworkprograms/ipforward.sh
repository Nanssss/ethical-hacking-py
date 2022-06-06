#!/bin/bash

if test $# -ne 1
then
echo "Il me faut un parametre"
exit 1
fi

arg=$1
echo $arg > /proc/sys/net/ipv4/ip_forward
echo "Valeur de ip_forward a $arg"
