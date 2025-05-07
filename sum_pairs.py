# write a program to  find all paris of integers whose sum is equal to a given number
# [2,6,3,9,11] , 9
# output => [1,2] => the index

#only +ve numbers

def sumPairs(arr, target):
    output = []
    for i  in range(len(arr)):
        for j in range(i+ 1, len(arr)): 
            if arr[i] + arr[j] == target:
                output.append([i,j])
    print(output) 

#testing 
print(sumPairs([5,2,6,3,9,11,4],9))
    