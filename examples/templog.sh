#!/bin/bash
#
# usage: templog.sh [delay] [count] 
#        delay: Waiting Time for next Acquisition 
#        count: Anzahl der Werte
#
#
for ((i=0; i < $2; i++))
do
 TEMP1=`date +%X%t%x` 
 TEMP2=`python3 gettemp.py`
 echo $TEMP1 $TEMP2 
 sleep $1
done
