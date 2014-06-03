#!/bin/bash
EXPECTED_ARGS=1
EXPECTED_ARG=2
E_BADARGS=65

if [ $# -lt $EXPECTED_ARGS ]
then
  	echo "Usage: `basename $0` binary [optional port #]"
  	exit $E_BADARGS
fi

if [ $# -ne $EXPECTED_ARG ]
then
	echo "PORT: 2323  Binary: $1"
	socat TCP-LISTEN:2323,reuseaddr,fork EXEC:./$1

else   
	echo "PORT: $2  Binary: $1"
	socat TCP-LISTEN:$2,reuseaddr,fork EXEC:./$1
fi
