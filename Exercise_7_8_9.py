#------List---------
testList = [1, 1, 2, 2.5]
print (len(testList))
testList.append(3)
testList.extend(testList)
#sort just use for int list
testList.sort() 
testList.sort(reverse = True)
deleteIndex = 1
testList.pop(deleteIndex)
testList.remove(3)
print(testList)
print(testList[2:])
#------Tuple---------
#the same list, it just add and cant be change
testTuple = (1, 1, 2, 2.5, 'helu')
#------Set---------
#The same list, but we cant add the same value which is alreay in the Set
testSet = {1, 2, 2.5, 'helu'}
#------Dict---------
#dict meant dictionary, it have key and value in one obj
testDict = {1: "MySQL", 2: "SQLServer", 3:"SQLite"}

testSet.add('helu')

print (testSet)

# *args is the same list or tuple
# **kwargs is the same dict 