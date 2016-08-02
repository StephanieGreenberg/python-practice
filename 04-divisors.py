num = int(raw_input("Please enter your number: "))

def check_divisors(num):
	lst = []
	for x in range(1,num + 1):
		if num % x == 0:
			lst.append(x)
	print lst
check_divisors(num)
