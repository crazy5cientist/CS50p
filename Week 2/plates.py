def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if not 2 <= len(s) <= 6:
        return False
    if not s[0:2].isalpha():
        return False
    for x, y in enumerate(s):
        if y == "0" and s[x-1].isalpha():
            return False
        if y.isnumeric() and x < len(s) -1 and s[x+1].isalpha():
            return False
    return True


main()