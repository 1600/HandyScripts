#/bin/bash
inotifywait -mq /home/sport --timefmt '%d/%m/%y %H:%M' --format '%w%f' -e create | while read -r line
do
   	 echo $line " was created by "$(ps aux | grep `lsof -nt $line` | awk '{print  $11 " " $12}')
done


#trap ctrl_c INT
#function ctrl_c() {
#        echo "** Trapped CTRL-C"
#		 sleep 2
#        pkill -f inotify
#         kill -15 $$
#}

#inotifywait -mrq . --timefmt '%d/%m/%y %H:%M' --format '%w%f' -e create > fileCreated.txt &
#declare -i linecount=0
#while true
#do
#	newlinecount=`wc -l fileCreated.txt | cut -d ' ' -f1`
#	if [ `wc -l fileCreated.txt | cut -d ' ' -f1` -gt $linecount ]; then
#		path=`tail -1 fileCreated.txt`
#		echo `lsof -nt $path`
#		linecount=$newlinecount
#	fi
#done