#!/bin/bash/python3

"""This is guessing game"""
try:
	guess_number = int(input("enter number: "))
	print(guess_number)
except ValueError:
	print("Only integer number is allowed")
except Exception:
	print("something went wrong!")