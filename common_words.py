# Input:
# An integer N
# N lines of text
# Task:
# Count all the words in all N lines and print the word that appears most often. 
# If there are multiple with the same frequency, print the one that comes first alphabetically.

# --- if input needed 
# N = int(input())
# lines = [input() for _ in range(N)]

#for testing
N = 3
lines = ["i like to i code in python",
"i python is named after a show named monty i python and not after the snake python",
"i think python is good i think python is more important than php"]


def common_words(lines):
    word_count = {}
    for line in lines: 
        word_list = line.split()
        for word in word_list:
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word] = 1

    print(word_count)
    max_count = max(word_count.values())
    # print(max_count)

    print(word_count.items())
    most_common = [word for word, count in word_count.items() if count == max_count] 
    
    print(most_common)
    return most_common[0]




print(common_words(lines))