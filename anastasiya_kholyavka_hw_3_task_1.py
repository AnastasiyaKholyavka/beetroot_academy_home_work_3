"""
anastasiya_kholyavka
HW_3_task_1

Make a program that has your name and the current day of the week 
stored as separate variables and then prints a message. 
Note that  <name> and <day> are predefined variables in source code.
An additional bonus will be to use different string formatting methods 
for constructing result string.

"""


# Без форматування

name = "Anastasiya"
day = "Sunday"

print("Good day," + " " + name + "!" + " " + day + " " + "is a perfect day to learn some python.")

# Old style % - Чому не працює?

name = "Anastasiya"
day = "Sunday"

#print("Good day," %(name)s %(!)c %(day)s "is a perfect day to learn some python.")

# Функція str.format()

name = "Anastasiya"
day = "Sunday"

print("Good day, {0}! {1} is a perfect day to learn some python.".format(name, day))

# f-strings

name = "Anastasiya"
day = "Sunday"

print(f"Good day, {name}! {day} is a perfect day to learn some python.")