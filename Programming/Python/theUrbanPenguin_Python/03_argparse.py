# this file demonstrates the functionality of adding via py file arguments

from datetime import date, timedelta
import os, crypt, sys
from termcolor import colored


# date time module
now = date.today()		# current date
end = timedelta(days=5) +  now	# adding 5 days to current date
expire = end.isoformat()	# make sure to have yyyymmdd format
#print("now {}, end {}, expriy in isoformat {}".format(now, end, end.isoformat()))

# create user with password and expiry of user
password = "Pass1"
encryptedPassword = crypt.crypt(password, "xyz")
if len(sys.argv) == 1:
    sys.exit("Not enough argument(s) provided!")
if os.getuid() == 0:
        os.system("useradd -p " + encryptedPassword + " -e" + expire + " " + sys.argv[1])
    print("check files: cat /etc/passwd (added user1) & tail /etc/shadow  (for expiry of user1)")
    os.system("tail /etc/passwd")
else:
    print(colored('you need be root to create the user!!!! Try sudo', 'red'))

print("\ndone")
