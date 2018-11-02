n = int(input())

test_cases = []
for _ in range(n):
    a = int(input())
    b = input()
    c = [int(x) for x in b if not x == ' ']
    test_cases.append((a,c))
    
for j in test_cases:
    x = 0
    y = len(j[1]) - 1
    temp = []
    valid = "Yes"
    while(x < y):
        if j[1][x] >= j[1][y]:
            if len(temp) > 0:
                if j[1][x] <= temp[-1]:
                    temp.append(j[1][x])
                    x+=1
                else:
                    valid = "No"
                    break
            else:
                temp.append(j[1][x])
        else:
            if len(temp) > 0:
                if j[1][y] <= temp[-1]:
                    temp.append(j[1][y])
                    x+=1
                else:
                    valid = "No"
                    break
            else:
                temp.append(j[1][y])
                
    print(valid)