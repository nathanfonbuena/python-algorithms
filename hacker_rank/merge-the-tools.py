from collections import OrderedDict 
def merge_the_tools(string, k):
    # Split the string into segments of length k
    segments = [string[i:i+k] for i in range(0, len(string), k)]

    non_duplications = ["".join(OrderedDict.fromkeys(i)) for i in segments]

    for i in non_duplications:
        print(i)

merge_the_tools("AABCAAADA", 3)