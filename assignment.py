#change 80 to 89 in the list
student_mark=[60,80,90,98 ]
student_mark[1]=89
print(student_mark)

#add anew item 55(append anew list)
student_mark=[60,80,90,98]
student_mark.append(55)
print(student_mark)

#find the size of the list having appended 55
print(len(student_mark))

#a python program to sum all the items in the list.
total= sum(student_mark)
print(total)

# a python function that takes two lists and returns true, if they have at least a common member
a= input("enter items")
b=input("enter items")
print("true,there are common numbers")