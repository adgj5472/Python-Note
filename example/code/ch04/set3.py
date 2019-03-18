# set
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("A = " + str(A))
print("B = " + str(B))

# intersection
C = A & B
print("A & B = " + str(C))
C = A.intersection(B)
print("A.intersection(B) = " + str(C))

# union 
C = A | B
print("A | B = " + str(C))
C = A.union(B)
print("A.union(B) = " + str(C))

# difference
C = A - B
print("A - B = " + str(C))
C = A.difference(B)
print("A.difference(B) = " + str(C))

# symmetric difference
C = A ^ B
print("A ^ B = " + str(C))
C = A.symmetric_difference(B)
print("A.symmetric_difference(B) = " + str(C))