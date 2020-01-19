"""
add or remove user(s) as command line arguments or from file
"""

import sys
import os
import crypt
import argparse
import datetime 

# Create user
def creatuser(user, expiredays):
	now = datetime.date.today()
	end = now + datetime.timedelta(days=expiredays)
	expiry = end.isoformat()
	print(expiry)
	password = "dummy"
	encPassword = crypt.crypt(password, "123")
	print(encPassword)
	os.system("useradd -p " + encPassword + " -e " + expiry + " " + user)
	os.system("tail /etc/passwd")

# Remove user
def removeuser(user):
	os.system("userdel " + user)
	os.system("tail /etc/passwd")

# Create / Remove users from file
def userfromfile(file, expiredays):
	userfile = file
	with open(userfile) as f:
		for user in f.readlines():
			if args.addfromfile:
				creatuser(user, expiredays)
			elif args.removefromfile:
				removeuser(user, expiredays)
	os.system("tail /etc/passwd")

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', nargs='+', help='Create User(s) via command line arguments')
parser.add_argument('-r', '--remove', nargs='+', help='Remove User(s) via command line arguments')
parser.add_argument('-af', '--addfromfile', help='Create User(s) from File')
parser.add_argument('-df', '--removefromfile', help='Remove User(s) from File')
parser.add_argument('-e', '--expiry', help='Expiry date of User')

args = parser.parse_args()

# if user is sudo
if os.getuid() == 0:
	
	if len(sys.argv) == 1:
		print("too few arguments! try help")

	# if enough arguments are provided
	else:
		if args.expiry:
			expiredays = args.expiry 
		else:
			expiredays = 5

	if args.add:
		for u in args.add:
			creatuser(u, expiredays)
	elif args.remove:
		for u in args.remove:
			removeuser(u)

	elif args.addfromfile:
		userfromfile(args.addfromfile, expiredays)
	
	elif args.removefromfile:
		userfromfile(args.removefromfile, expiredays)

else:
	print("try sudo!")

print("\ndone!")