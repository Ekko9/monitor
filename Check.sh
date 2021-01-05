#!/bin/bash
cd $(dirname $0)
num=80
ip_list=`cat IP.txt`
for i in ${ip_list}
do
	for j in `./autossh.sh user password $i 'df -h' 2>/dev/null | grep /opt |awk  '{print $5}' | sed 's/.$//'`
        do
        	if [ ${j} -gt ${num} ]
        	then
            		echo ${i}_${j}
            		python3 SendMail.py ${i}
			break
       		 fi
    	done
done
