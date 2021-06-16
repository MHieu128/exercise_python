listInt = [1, 2, 3, 4, 5]
newlist = [x**2 for x in listInt if int(x) % 2 == 0]
print(newlist)