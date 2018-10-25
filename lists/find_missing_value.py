def find_missing_value(given_list):
    # Sort the given list
    given_list.sort()

    # Loop through the list and check if val + 1 exists
    for idx, val in enumerate(given_list):
        if idx + 1 < len(given_list) and not given_list[idx + 1] == val + 1:
            return val + 1

    # If the loop finishes without return a number the list is complete
    return None

test_data = [7,9,10, 6,5,11,12]
fail_data = [7,9,10,8,6,5,11,12]

print(find_missing_value(test_data))
print(find_missing_value(fail_data))