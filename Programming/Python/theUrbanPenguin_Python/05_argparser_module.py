# arg parser usage

#anaconda3/bin/python3

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-a", "--add", nargs="+", help = "Create user(s)")
# parser.add_argument("-d", "--delete", nargs="+", help = "Delete user(s)")
# args = parser.parse_args()



# # adding user
# if args.add:
# 	for u in args.add:
# 		print("Creating user " + u)

# # deleting user
# if args.delete:
# 	for u in args.delete:
# 		print("Deleting user " + u)
#--------------------------------------------------------------------------------------------
# this file demonstrates the functionality of adding number of users from arguments 

# from datetime import date, timedelta
# import os, crypt, sys, argparse
# from termcolor import colored

# if len(sys.argv) == 1:	# if no args provided
# 	sys.exit("Not enough argument(s) provided!")

# parser = argparse.ArgumentParser()
# parser.add_argument("-a", "--add", nargs="+", help = "Create user(s)")
# parser.add_argument("-d", "--delete", nargs="+", help = "Delete user(s)")
# args = parser.parse_args()


# # date time module
# now = date.today()		# current date
# end = timedelta(days=5) +  now	# adding 5 days to current date
# expire = end.isoformat()	# make sure to have yyyymmdd format
# #print("now {}, end {}, expriy in isoformat {}".format(now, end, end.isoformat()))

# # create user with password and expiry of user
# password = "Pass1"
# encryptedPassword = crypt.crypt(password, "xyz")

# if os.getuid() == 0:	# only if you are sudo/ priviliged user
# 	if args.add:
# 		for u in args.add:
# 			print("Creating user " + u)
# 			os.system("useradd -p " + encryptedPassword + " -e" + expire + " " + u) # adding user with expiry time
# 	if args.delete:
# 		for u in args.delete:
# 			print("Deleting user " + u)
# 			os.system("userdel -r "  + u) # remove user

# 	print("check files: cat /etc/passwd")
# 	os.system("tail /etc/passwd")
# else:
# 	print(colored('you need be root to create the user!!!! Try sudo', 'red'))

# print("\ndone")

#--------------------------------------------------------------------------------------
# this file demonstrates the functionality of adding number of users from arguments or from a file

from datetime import date, timedelta
import os, crypt, sys, argparse
from termcolor import colored

if len(sys.argv) == 1:	# if no args provided
	sys.exit("Not enough argument(s) provided!")

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs="+", help = "Create user(s)")
parser.add_argument("-d", "--delete", nargs="+", help = "Delete user(s)")
parser.add_argument("-f", "--file", help = "user(s) file")

args = parser.parse_args()


# date time module
now = date.today()		# current date
end = timedelta(days=5) +  now	# adding 5 days to current date
expire = end.isoformat()	# make sure to have yyyymmdd format
#print("now {}, end {}, expriy in isoformat {}".format(now, end, end.isoformat()))

# create user with password and expiry of user
password = "Pass1"
encryptedPassword = crypt.crypt(password, "xyz")

if os.getuid() == 0:	# only if you are sudo/ priviliged user
	if args.add:
		for u in args.add:
			print("Creating user " + u)
			os.system("useradd -p " + encryptedPassword + " -e" + expire + " " + u) # adding user with expiry time
	elif args.delete:
		for u in args.delete:
			print("Deleting user " + u)
			os.system("userdel -r "  + u) # remove user
	elif args.file:
		userfile = args.file
		with open(userfile) as f:
			for l in f.readlines():
				if l == "\n":
					continue
				l = l.strip("\n")
				print("Creating user " + l)
				os.system("useradd -p " + encryptedPassword + " -e" + expire + " " + l) # adding user with expiry time


	print("check files: cat /etc/passwd")
	os.system("tail /etc/passwd")
else:
	print(colored('you need be root to create the user!!!! Try sudo', 'red'))

print("\ndone")
