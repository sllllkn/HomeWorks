def popular_words(text, words):
    text = text.lower()
    text_words = text.split()

    result = {}
    for word in words:
        count = 0
        for item in text_words:
            if item == word:
                count += 1
        result[word] = count
    return result