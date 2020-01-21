# """ bash variable examples"""
#!/bin/bash

########################
# #  how to declare simple variables

#echo "Hello World!"
#PRICE_PER_APPLE=5
#MyFirstLetters=ABC
#greeting='Hello		World!'

#echo "The price of an apple is: \$$PRICE_PER_APPLE"

#echo "The first 10 alphabet letters: ${MyFirstLetters}DEFGHIJ"

#echo $greeting
#echo -e "now in double quotes preserve spacing:\n $greeting"

########################################################
# # declare variable using  commands, e.g. ls or date 

#FL=`ls /home/ali/Desktop/`
#echo $FL

#FileWithTimeStamp=/home/ali/Desktop/Bash/file_$(/bin/date +%Y-%m-%d).txt
# generate file
#touch $FileWithTimeStamp

##################################################
# # Variables per command line
# BIRTHDATE="Jan 1, 2000"
# PRESENTS=10
# BIRTHDAY=`date -d "$BIRTHDATE" +%A`

# if [ "$BIRTHDATE" == "Jan 1, 2000" ] &&  [ "$BIRTHDAY" == "Samstag" ] && [[ $PRESENTS = 10 ]] ; then
# 	echo "I was born on $BIRTHDATE. It was $BIRTHDAY, and I got $PRESENTS presents!!!"
# else
# 	echo "not correct."
# fi

# if [ $1 -gt 100 ]
# then
# 	echo "hey that's a large number"
	
# 	if (( $1 % 2 == 0 ))
# 	then
# 		echo "and an even number too!"
# 	fi
# fi

# echo "this is the file name is $0, and it is argument \$0 in Bash."

is_alive_ping()
{
	ping $1 -c 1 > /dev/null
	[ $? -eq 0 ] && echo Node with IP: $i is up
}

for i in 192.168.178.{1..99}
do	is_alive_ping $i
	# ping 192.168.1.$i -c 1
done
exit
