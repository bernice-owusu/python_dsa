# "Write a function in Python that analyzes the sentiment of a sentence 
# and returns whether it's positive, negative, or neutral."
# Example usage
# print(analyze_sentiment("I love this product, it's fantastic"))  # Positive
# print(analyze_sentiment("This is a horrible experience."))        # Negative
# print(analyze_sentiment("It is okay, nothing special."))          # Neutral
# positive_words = {'happy', 'great', 'excellent', 'good', 'love', 'awesome', 'fantastic'}
# negative_words = {'bad', 'terrible', 'awful', 'hate', 'sad', 'horrible', 'poor'}

## soln 
# 1 --> This is a horrible experience. --> ["This", "is", "a" , "horrible", "experience"] 
# 2 -- > check the count of pos words --> [word in pos_words for word in words]
# 3 -- > check the count of neg words --> [word in neg_words for word in words]
# 4 --> check  to return pos. neg or neutral

def analyze_sentiment(sentence,pos_words,neg_words):
    words = sentence.lower().split()
    # print(words)
    pos_count = sum(word in pos_words for word in words)
    neg_count = sum(word in neg_words for word in words)
    print(pos_count, neg_count)
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"
    
    
print(analyze_sentiment("I love this product, it's fantastic!", ['happy', 'great', 'excellent', 'good', 'love', 'awesome', 'fantastic'], ['bad', 'terrible', 'awful', 'hate', 'sad', 'horrible', 'poor']))