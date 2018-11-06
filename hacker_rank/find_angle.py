import math 

ab = int(input())

bc = int(input())

length = math.sqrt(ab**2 + bc**2)

c = ab/length

what = math.asin(c)

print(round(math.degrees(what)),chr(176), sep="")