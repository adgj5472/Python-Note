# list
# using index
list1 = [1, 2, 3, 4, 5, 6]
print(list1[0])   # 1
print(list1[1])   # 2
print(list1[-1])  # 6
print(list1[-2])  # 5
list1[1] = 10     # change value
print(list1)

list1 = [1, 5]
print("list1 = " + str(list1))

# append new item
list1.append(7)
print("list1.append(7) = " + str(list1))
list1.extend([9, 11, 13])
print("list1.extend([9,11,13]) = " + str(list1))

# insert new item
list1.insert(1, 3)
print("list1.insert(1,3) = " + str(list1))

# delete item
del list1[2]
print("del list1[2] = " + str(list1))
e1 = list1.pop()
print("e1 = list1.pop() = " + str(list1))
print("e1 = " + str(e1))
e2 = list1.pop(1)
print("e2 = list1.pop(1) = " + str(list1))
print("e2 = " + str(e2))
list1.remove(9)
print("list1.remove(9) = " + str(list1))
