list={}
while True:
	try:
		item = input("")
		if item in list:
			list[item] +=1
			continue
		else:
			list[item] = 1
			continue
	except EOFError:
		break
for name, number in list.items():
	print(number, name.upper())
