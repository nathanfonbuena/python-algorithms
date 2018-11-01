from itertools import groupby 
from collections import OrderedDict 

vals = input()

lst_version = [str((len(list(g)), int(k))) for k,g in groupby(vals)]

print(" ".join(lst_version))