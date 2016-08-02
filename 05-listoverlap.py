import random

def generateRandomList():
	lst = []
	rand = random.randint(1, 20)
	for i in range(rand):
		lst.append(random.randint(1, 100))
	return lst

lst1 = generateRandomList()
lst2 = generateRandomList()

def check_overlap():
	print lst1
	print lst2
	lst = []
	for item in lst1:
		if item in lst2:
			lst.append(item)
	print lst

check_overlap()
