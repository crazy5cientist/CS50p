def main():
    time = input("What time is it? ")
    z = convert(time)
    if z >= 7 and z <= 8:
        print("Breakfast time")
    elif z >= 12 and z <= 13:
        print("Lunch time")
    elif z >= 17 and z <= 18:
        print("Dinner time")
              
def convert(time):
    hour, minute = time.split(":")
    minute = int(minute) / 60
    z = int (hour) + minute
    return (z)

main()