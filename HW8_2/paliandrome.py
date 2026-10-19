def is_palindrome(text):
    text = text.lower()
    letters = ""
    for ch in text:
        if ch.isalnum():
            letters += ch

    left = 0
    right = len(letters) - 1
    while left < right:
        if letters[left] != letters[right]:
            return False
        left += 1
        right -= 1
    return True


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("OK")