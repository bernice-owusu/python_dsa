# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

def get_middle(s):
    length = len(s)
    if(len(s) == 1):
        return s
    elif (len(s)%2 == 0):
        return s[(length-1) - (length//2)] + s[length - (length//2)]
    else:
        return s[length - (length//2 + 1)]
        

print(get_middle("A"))

# Second Soln
def get_middle(s):
    x = len(s)
    y = int(x/2)
    if(len(s) == 1):
        return s
    elif (x%2 == 0):
        return s[y-1:y+1]
    else:
        return s[y:y+1]