
import string

def generate_hashtag(text):
    words = text.split()

    hashtag = "#" + "".join(word.capitalize() for word in words)

    hashtag = "".join(char for char in hashtag if char not in string.punctuation.replace("#", ""))

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


print(generate_hashtag("Python Community"))
print(generate_hashtag("i like python community!"))
print(generate_hashtag("Should I, I subscribe? Yes!"))
