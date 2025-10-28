while True:
	try:
		fuel = input("Fraction: ")
		x, y = fuel.split("/")
		x = int(x)
		y = int(y)
		if x==0 or x>y or x/y < 0:
			continue
	except ValueError:
		pass
	else:
		break
if x/y>0.99:
	print("F")
elif x/y<0.01:
	print("E")
else:
	print(f"{round((x/y)*100)}%")