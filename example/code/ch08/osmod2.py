# modules
import os

fname = os.path.realpath("osmod2.py")

print(fname)
r = os.path.split(fname)
print("os.path.split() =", r)
r = os.path.splitext(fname)
print("os.path.splitext() =", r)
p = os.path.dirname(fname)
print("p = os.path.dirname() =", p)
f = os.path.basename(fname)
print("f = os.path.basename() =", f)
r = os.path.join(p, f)
print("os.path.join(p,f) =", r)