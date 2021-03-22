Num1 = int(input("Enter a number:"))
Num2 = int(input("Enter another number:"))
operation = input("What operation do you want it? (mul/div/mod)");
if (operation == "mul"):
	print(Num1*Num2)
elif (operation == "div"):
	print(Num1/Num2)
elif (operation == "mod"):
	print(Num1%Num2)
else:
	print("Invalid")

