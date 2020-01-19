# File to show for loops
import sys

for m in sys.modules:
	print(m) 	#print modules names in system modules

print(len(m))		#print length i.e. number of system moduels

# Open file within python, print contents (lines)

with open("01_textfile") as file:
	for l in file:
		if (l.split()[0] == "January"):
			print("won't print January")
			continue	#if January, don't print
		else:
			print(l, end="")	#else print all lines
