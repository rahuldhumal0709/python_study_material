num1=10
num2=20
try:
	res = num1 + num2
	print(res)
except TypeError:
	print("Error: cannot add an int and a str")