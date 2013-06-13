#!/bin/bash
for ((i=0; i < $2; i++))
do
 TEMP1=`date +%X%t%x` 
 TEMP2=`python3 gettemp`
 TEMP2=`python3 gettemp`
 echo $TEMP1 $TEMP2 
 sleep $1
done
