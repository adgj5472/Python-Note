# set
s1 = {1, 5}
print("s1 = " + str(s1))

# add item
s1.add(7)
print("s1.add(7) = " + str(s1))
s1.update([9, 11, 13])
print("s1.update([9,11,13]) = " + str(s1))
s1.update([2, 3], {4, 6, 10})
print("s1.update([2,3],{4,6,10}) = " + str(s1))

# remove item
s1.discard(2)
print("s1.discard(2) = " + str(s1))
s1.remove(6)
print("s1.remove(6) = " + str(s1))
e1 = s1.pop()
print("e1 = s1.pop() = " + str(s1))
print("e1 = " + str(e1))
s1.clear()
print("s1.clear() = " + str(s1))