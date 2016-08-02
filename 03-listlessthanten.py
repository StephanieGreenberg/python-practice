import random

def generateRandomList():
	lst = []
	rand = random.randint(1, 10)
	for i in range(rand):
		lst.append(random.randint(1, 20))
	return lst
def  getLessThanFive(lst):
	print lst
	for i in lst:
		if i < 5:
			print i

getLessThanFive(generateRandomList())
