marks={
    "prabhat": 100 ,
    "shubham": 56 ,
    "harry": 45 ,
    "ravi":90 ,
    0:"tarun"
} 
print(marks.items()) #marks.itemis a methods to seprately shows items.it shows result in form of tuples
print(marks.keys())# for example "prabhat is a key "
print(marks.values()) # for example 100 is a value 
marks.update({"prabhat":99 ,"renuka":100})# t is also ued to add items on dictionariesprint(marks)
print(marks.get("shinchan"))#it wil give error because shinchan doesnt exist in marks  
print(marks.get("prabhat")) # you will see here after running it you will get 99 beacuse you updated the marks
# you will get 100 if you comment out the update line
#print(marks["harry2"])# gives error
print(marks.pop("ravi"))# by commneting out all other codes you will that ravi in results is not in .
print(marks)

print(marks.popitem()) # it removes the last inserted item on the dict. and removes it
print(marks)