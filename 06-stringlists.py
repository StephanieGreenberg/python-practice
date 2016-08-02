from math import floor, ceil

string = ((raw_input("Please enter a string: ").replace(" ", "")).lower())

def is_palindrome(str):
	str1 = (str[0:int(floor(len(str)/2))])[::-1]
	if len(str) % 2 == 0:
	 	str2 = str[int(ceil(len(str)/2)):len(str)]
	else:
	 	str2 = str[int(ceil(len(str)/2) + 1):len(str)]
	if str1 == str2:
	  	print True
	else:
	 	print False

is_palindrome(string)