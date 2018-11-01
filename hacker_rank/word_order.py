from collections import OrderedDict
num_of_vals = int(input())

words = []

for _ in range(num_of_vals):
    words.append(input())
    
unique = OrderedDict()

for i in words:
    if not i in unique:
        unique[i] = 1
    else:
        unique[i] += 1
        
print(len(unique))
result = "" 

for k,v in unique.items():
    result += str(v) + " "

print(result)