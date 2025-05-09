# "Given a list of numbers, find the number whose digits add up to the highest total. "
# "If two numbers have the same total, choose the bigger number."

# [12, 33, 44, 21] ==> sum_of_the digits ==> [3,6,8,3] ==> return 44
# [36, 33, 12,54] ==> sum_of_the_digits ==> [9,6,3,9] ==> [36,54] ==> 54

# loop over ==> [] ==> get the sum ==> store it (dict) ==> return the highest 

def heaviest_num(myList):
    results = {}
    for val in myList:
        pair_str = list(str(val))
        pair = list(map(int,pair_str))
        pair_sum = sum(pair)

        results[val] = pair_sum
    max_val = max(results.values())

    output = max(key for key,val in results.items() if val == max_val)
    return output
      
print(heaviest_num([51,100,25,2345]))