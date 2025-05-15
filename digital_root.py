# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#Examples
#    16  -->  1 + 6 = 7
#   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    results = 0
    n_str = list(str(n))
    n_list = [int(val) for val in n_str]
    n_sum = sum(n_list)
    # print(n_list)
    # print(n_sum)
    
    if(n_sum >= 10):
        results = digital_root(n_sum)
        return results
    else:
        return n_sum
   
    
    
    
print(digital_root(493193))