y = 50
while y > 0:
    print("Amount Due:", y)
    x = int(input("Insert Coin: "))
    if x in [5, 10, 25]:
        y = y - x
if y < 0:
	print("Charge Owned", abs(y))