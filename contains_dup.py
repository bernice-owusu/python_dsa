# Contains duplicate
# given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every ele is distinct
#
# Example
# Input: nums = [1,2,3,1]
# Output: true 

def contains_dups(nums):
    return False if len(set(nums)) == len(nums) else True

print(contains_dups([1,2,3,17]))