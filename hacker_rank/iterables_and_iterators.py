from itertools import combinations
n = int(input())

str_list = input().replace(" ", "")

split_group = int(input())

results = list(combinations(str_list, split_group))

count = 0

for r in results:
    if 'a' in r:
        count += 1
    
print(count/len(results))