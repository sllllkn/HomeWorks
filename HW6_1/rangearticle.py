
import string

def between_letters(text):
    start, end = text.split("-")
    letters = string.ascii_letters

    start_index = letters.index(start)
    end_index = letters.index(end)

    return letters[start_index:end_index + 1]


print(between_letters("a-c"))
print(between_letters("a-a"))
print(between_letters("s-H"))
print(between_letters("a-A"))
