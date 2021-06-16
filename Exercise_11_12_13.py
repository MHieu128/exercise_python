# w: if file not exits, create new one
#create and write somethings
file = open('fileTest.txt', 'w')
file.write("Hieulm13 just test!")
file.close()

#read and show
file = open('fileTest.txt', 'r')
#1st way to do
for x in file:
  print(x)
#2nd way to do
print(file.read())
file.close()

#write to the lastet cursor of file, not override
file = open('fileTest.txt', 'a')
file.write("Hieulm13 just test!")
file.close()