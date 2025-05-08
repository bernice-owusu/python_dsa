# Write a function reverse_list that takes a list of integers and returns a new list with the elements in reverse order.

def reverse_list(myList):
    return myList[::-1]
    
print(reverse_list([1, 2, 3, 4]))



# Write a function remove_duplicates that takes a list and returns a new list with duplicates removed, preserving the original order.
def remove_dup(arr):
    mySet = set()
    output = []
    for i in arr:
        if i not in mySet:
            output.append(i)
            mySet.add(i)
    return output
            
    
print(remove_dup([9, 1, 2, 2,0, 3, 4, 4, 5]))


# Write a function rotate_left that rotates a list to the left by k positions.
def rotate_left(arr,k):
    list_rotate = arr[0:k]
    remaining_arr = arr[k: ]
    remaining_arr.extend(list_rotate)
    return remaining_arr
    
    
print(rotate_left([1, 2, 3, 4, 5], 2) )




# Write a function find_second_largest that returns the second largest number in a list.
#
# Example:
# find_second_largest([10, 20, 4, 45, 99])  # Output: 45
# Handle cases where the list has duplicates or less than 2 unique numbers (you can return None in such cases). Go ahead!

def find_second_largest(arr):
    #remove duplicates
    unique_list = list(set(arr))
    
    # handle edge case
    if len(unique_list) < 2:
        return None
        
    # sort in desc order
    sorted_arr =  sorted(unique_list, reverse= True)
    
    # return the second highest
    return sorted_arr[1]
    

print(find_second_largest([10, 20, 4, 45, 99]))
    