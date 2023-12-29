list_values = []
lens_value = []

list_values.append(input("Fname"))
list_values.append(input("Lname"))
list_values.append(input("Birth"))
list_values.append(input("Mail"))
list_values.append(input("Phone"))

lens_value.append(len(list_values[0]))
lens_value.append(len(list_values[1]))
lens_value.append(len(list_values[2]))
lens_value.append(len(list_values[3]))
lens_value.append(len(list_values[4]))

for i in range(len(list_values)):
	if len(list_values[i]) != max(lens_value):
		for j in range(max(lens_value)-len(list_values[i])):
			list_values[i]=list_values[i] + " "

for i in range(len(list_values)):
	print(list_values[i])

ramka = len("║ Ім'я:" + list_values[0] + "   Прізвище:" + list_values[1] + "║")-2
print("╔", end="")
print("═"*ramka, end="")
print("╗")
print("║ Ім'я:" + list_values[0] + "   Прізвище:" + list_values[1] + "║")
print("║ Рік: " + list_values[2] + "   E-mail:  " + list_values[3] + "║")
print("║      " + len(max(list_values))*" " + "   Phone:   " + list_values[4] + "║")
print("╚", end="")
print("═"*ramka, end="")
print("╝")