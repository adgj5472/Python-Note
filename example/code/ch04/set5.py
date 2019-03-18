# set
A = {1, 2, 3}
B = {4, 5, 6, 7, 8}
print("A = " + str(A))
print("B = " + str(B))
print(A.isdisjoint(B))

C = {1, 2, 3}
D = {1, 2, 3, 7, 8}
print("C = " + str(C))
print("D = " + str(D))
print(C.issubset(D))
print(C.issuperset(D))

E = {1, 2, 3, 5, 6}
F = {1, 2, 3}
print("E = " + str(E))
print("F = " + str(F))
print(E.issubset(F))
print(E.issuperset(F))

G = frozenset([1, 2, 3, 1, 5, 6])
H = {1, 2, 3}
print("G = " + str(G))
print("H = " + str(H))
print(G.issuperset(F))
G.add(9)