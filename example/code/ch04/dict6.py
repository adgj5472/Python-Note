# dictionary
d1 = {"tom":"02-11111111",
      "bob":"02-22222222",
      "mike":"02-33333333"}
print("d1 = " + str(d1))

i = d1.get("tom")
print("d1.get('tom') = " + str(i))

i = d1.get("mary", "NA")
print("d1.get('mary', 'NA') = " + str(i))

t1 = d1.keys()
print("d1.keys() = " + str(t1))
list1 = list(t1)
for i in list1:
    print(i, end=" ")
print()

t1 = d1.values()
print("d1.values() = " + str(t1))
list1 = list(t1)
for i in list1:
    print(i, end=" ")