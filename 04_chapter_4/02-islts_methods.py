friends=["apple","akash",5,34.5,"prabhat","grapes"]

friends.append("nikhil")#append is a method which at the end of the list ads the string which you ant to add
print(friends)

l1=[12,8756,98,546,23]

l1.sort() # sort is a kind of methods which will set the numbers
print(l1)#in incresing orders 

l2=[12,8756,98,546,23]
l2.reverse()# it jus reverse your list
print(l2)

l3=[12,8756,98,546,23]
l3.insert(1,11211)# by using methhod "insert"you an insert anything in you list 
#but first write from wheere you have to insert
print(l3)

l4=[12,33,98,44,23]
l4.pop(2) #only remove item in list 

print(l4.pop(2))#Remove and return item at index (default last).
l5=[12,8756,98,546,23]
l5.remove(12)
print(l5)

l6=[12,8756,98,546,23]
l6.clear()#this methd clears all the items on list
print(l6)