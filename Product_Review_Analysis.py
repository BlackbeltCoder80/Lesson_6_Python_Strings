# Task 1: Keyword Highlighter

#Write a program that searches through reviews list and looks for keywords such as 
# "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]
# Iterate through each review
for user_review in reviews:
    for user_keyword in keywords:
        user_review = user_review.replace(user_keyword, user_keyword.upper())
    print(user_review)  # Print the modified review

# I had to write this in notepad several times to figure it out. somehow I was in a infinite loop.
# The solution was removing the while loop. I was trying to make it so the program checked new reviews 
# that would be input by users. I didnt figure it out. So i stuck with the above code.
#So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for count_review_1 in positive_words:
    for count_review_2 in negative_words:
        positive_count = sum(count_review_1.lower().count(count_review_1) for positive_words in reviews)
        negative_count = sum(count_review_2.lower().count(count_review_2) for negative_words in reviews)

    #print(f"There are {positive_words} in the reviews")
    #print(f" There are {negative_count} in the reviews")
print(f"Postive Reviews: {positive_count}")
print(f"Negative Reviews: {negative_count}")
#Task 3: Review Summary

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

#Example: "This product is really good. I'm...",


for user_review in reviews:
    review_30_char = user_review[:30]
    last_space_index = review_30_char.rfind(" ")
    summary = review_30_char[:last_space_index]
    summary += "..."
    print(summary)

