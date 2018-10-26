def maximize(given_list, k, m):
    option_pool = []
    indexes = []
    
    for i in range(k):
        indexes.append(1)
    
    maximize.biggest_val = 0 


    def recurse(values, idx, m):
#       Sum is used to calculate the current value
        sum = 0 
        
        # Get the sum based off of our idx list
        for i, val in enumerate(idx):
            sum += (values[i][val] ** 2)
            
        #Calculate the value
        r = sum % m

        # If this is currently the biggest value set it as the new max 
        if r > maximize.biggest_val:
            maximize.biggest_val = r
        
        #if the value calculated is one less than the modulus than it is by
        #definition the largest value we can achieve and is the answer
        if r == m - 1:
            return r 
        
        # This loop checks to see if we have reached the end of recursion and stops
        # further recursive calls
        stop = []
        for i, val in enumerate(idx):
            if val == len(values[i]) - 1:
                stop.append(True)
            else:
                stop.append(False)
        
        if not False in stop:
            return r

        # i is the index of idx moving backwards
        for i in range(len(idx) - 1, -1, -1):
            if idx[i] < len(values[i]) - 1:
                idx[i] += 1
                try:
                    return recurse(values, idx, m)
                except RecursionError:
                    # If we hit the max resursvie depth we throw a hail mary and hope that the answer is 
                    # the modulus minus one
                    maximize.biggest_val = m - 1
                    return 
            else:
                idx[i] = 1
                continue
                
    recurse(given_list, indexes, m)
    
    return maximize.biggest_val


# k=3
# m=1000
# value_list = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]]


k=7 
m = 867
value_list = [
[7, 6429964, 4173738, 9941618, 2744666, 5392018, 5813128, 9452095],
[7, 6517823, 4135421, 6418713, 9924958, 9370532, 7940650, 2027017],
[7, 1506500, 3460933, 1550284, 3679489, 4538773, 5216621, 5645660],
[7, 7443563, 5181142, 8804416, 8726696, 5358847, 7155276, 4433125],
[7, 2230555, 3920370, 7851992, 1176871, 610460, 309961, 3921536],
[7, 8518829, 8639441, 3373630, 5036651, 5291213, 2308694, 7477960],
[7, 7178097, 249343, 9504976, 8684596, 6226627, 1055259, 4880436],
]

print(maximize(value_list, k, m))