import datetime

now = datetime.datetime.now()
name = raw_input("Please enter your name: ")
age = int(raw_input("Please enter your age: "))

#function calculates which year the user will turn 100
def calculate_100_year(age, now):
	return now.year + (100 - age)

print "%s, you will be 100 years old in %d. Happy early birthday!" % (name, calculate_100_year(age, now))
