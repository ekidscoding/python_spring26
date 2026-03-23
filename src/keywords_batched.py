from itertools import batched
from keyword import kwlist, softkwlist

for k in batched([*kwlist,*softkwlist], 5):
    print(*k, sep=", ")

