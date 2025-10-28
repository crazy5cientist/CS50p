inp = input("Input: ")
out = ""
for i in inp:
    if i.lower() in ["a", "o", "i", "e", "u"]:
        pass
    else:
        out = out + i
print("Output:", out)