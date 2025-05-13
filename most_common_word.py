#  Count all the words in all N lines and print the word that appears most often. 
# If there are multiple with the same frequency, print the one that comes first alphabetically.

# example
# N = 3
# lines = [ 
#         "i like to code in python",
#         "python is named after a show named monty python and not after the snake python",
#         "i think python is good i think python is more important than php"]

# results = {i: 3, like: 4 ...}

# line --> split() --> store in dict --> get the key that has the most value count 

def most_common_word(lines):
    result = {}
    for line in lines:
        line_list = line.split()
        for word in line_list:
            # print(word)
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    print(result)
    max_val = max(result.values())
    print(max_val)

    output = min(word for word,count in result.items() if count == max_val)
    print(output)
    return output

        

print(most_common_word(["i like to code in python","python is named after a show named monty ant ant ant ant ant ant  python and not after the snake python","i think python is good i think python is more important than php zip zip zip zip zip zip"]))