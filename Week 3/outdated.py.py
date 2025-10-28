months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
	try:
		date = input("Date: ")
		mdy = date.split("/")
		if len(mdy) == 3 and int(mdy[0]) <= 12 and 0 <= int(mdy[1]) <= 31 and mdy[2].isdigit():
			print(f"{mdy[2]}-{mdy[0]:02}-{mdy[1]:02}")
			break
	except ValueError:
		pass
	try:
		mdy1 = date.replace(",", "").split(" ")
		if len(mdy1) == 3:
			if mdy1[0] in months and 0 <= int(mdy1[1]) <= 31 and mdy1[2].isdigit():
				mm = months.index(mdy1[0]) + 1
				print(f"{mdy1[2]}-{mm:02}-{int(mdy1[1]):02}")
				break
			else:
				continue
	except ValueError:
			continue
				