""" Following code demonstrates the functionality of adding and deleting multiple users from command line arguments or from a file """

from datetime import date, timedelta
from termcolor import colored
import os
import crypt
import sys
import argparse


def adduser(users, expiredays):	
	# date time module
	users = users.lower()
	now = date.today()		# current date
	end = timedelta(days=expiredays) +  now	# adding 5 days to current date
	expire = end.isoformat()	# make sure to have yyyymmdd format

	# create user with password and expiry of user
	password = "Pass"
	encryptedPassword = crypt.crypt(password, "123")
	print("Creating user " + users)
	os.system("useradd -p " + encryptedPassword + " -e " + expire + " " + users)

def deluser(users):
	print("Deleting user " + users)
	os.system("userdel -r "  + users) # removing user

def usersfromfile(file, expiredays):
	with open(file) as f:
		for userline in f.readlines():
			if userline == "\n":
				continue
			userline = userline.rstrip()
			if args.addfromuserfile:	
				adduser(userline, expiredays)	
			elif args.deletefromuserfile:	
				deluser(userline)			

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs="+", help = "Create user(s)")
parser.add_argument("-d", "--delete", nargs="+", help = "Delete user(s)")
parser.add_argument("-e", "--expire", type=int, help = "Expiry days of user(s)")
parser.add_argument("-af", "--addfromuserfile", help = "add user(s) from a file")
parser.add_argument("-df", "--deletefromuserfile", help = "delete user(s) from a file")
args = parser.parse_args()

if os.getuid() == 0:	# only if you are sudo/ priviliged user
	if len(sys.argv) == 1:	# if no args provided
		sys.exit("Not enough argument(s) provided! try \"sudo python3 " + sys.argv[0] + " --help\"")
	
	if args.expire:
		expiredays = arg.expire
	else:
		expiredays = 5

	if args.add:
		for u in args.add:
			adduser(u, expiredays)
	
	elif args.delete:
		for u in args.delete:
			deluser(u)
	
	elif args.addfromuserfile:
		usersfromfile(args.addfromuserfile, expiredays)
	
	elif args.deletefromuserfile:
		usersfromfile(args.deletefromuserfile, expiredays)		

	# print("check files: cat /etc/passwd")
	os.system("tail /etc/passwd")

else:
	print(colored('you need be root to create the user!!!! Try sudo', 'red'))

print("\ndone")
