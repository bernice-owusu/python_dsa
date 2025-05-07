# Find the maximum product of two integers in an array where all elements are positive

arr = [1,7,3,4,9,5]

#solution 1
def max_product(arr):
    #sort array in desc order
    sorted_array = sorted(arr, reverse=True)

    #get the two max numbers
    max_nums = sorted_array[0:2] 

    #return the product
    return max_nums[0] * max_nums[1]

print(max_product(arr))


#solution 2 
def max_product2(arr):
    results = []
    for i in range(len(arr)): 
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            results.append(product)
    print(results)
    return max(results)

print(max_product2(arr))