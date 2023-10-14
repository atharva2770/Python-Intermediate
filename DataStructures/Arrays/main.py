from array import *

vals = array('i', [5, -9, 8, 4, 2, 7])

# for i in range(6):
#     print(vals[i])

# for e in vals:
#     print(e)

# for i in range(len(vals)):
#     print(vals[i])

valu = array(vals.typecode, (a*a for a in vals))

for e in valu:
    print(e)
