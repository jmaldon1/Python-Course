
#Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
	("James", "9/8", True, 9),
	("Shawna", "12/6", True, 22),
	("Amaya", "28/2", False, 8),
	("Kamal", "29/4", True, 19),
	("Sam", "16/7", False, 22),
	("Xan", "14/3", False, 34),
)

#Problem 1: Celebrations
#Loop through all of the people in BIRTHDAYS
#If they celebrate their birthday, print out
#"Happy Birthday" and their name
for person in BIRTHDAYS:
	if person[2]:
		print("Happy Birthday, {}".format(person[0]))