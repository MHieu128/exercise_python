import os
if os.path.exists("fileTest.txt"):
  os.remove("fileTest.txt")
else:
  print("The file does not exist")