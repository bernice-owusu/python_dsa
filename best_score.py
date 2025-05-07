# Given a list, write a function to get first and second best scores from the list
# List may contain duplicates

# Example 
myList = [84,85,86,87,85,90,85,83, 23, 90, 87, 87,87 ,45, 84, 1,2, 0]

# solution 1 

def first_second(my_list):
    # remove duplicates
    unique_nums = set(my_list)

    # reverse set into a list
    dup_removed = list(unique_nums)

    # sort list in desc order
    sorted_array = sorted(dup_removed, reverse=True)

    # get the first two items
    results = sorted_array[0:2]

    return results


print(first_second(myList))



# solution 2
myList = [84,85,86,87,85,90,85,83, 23, 90, 87, 87,87 ,45, 84, 1,2, 0]

def first_sec(myList):
    max1 = 0
    max2 = 0

    for i in range(len(myList)):
        if myList[i] > max1:
            max2 = max1
            max1 = myList[i]
    return max1, max2

print(first_sec(myList))
