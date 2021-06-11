"""
2. How do you print the first non-repeated character from a string?
"""
print("START!!\n...")


def implementation(text):
    for x in list(text):
        if text.count(x) == 1:
            return x
    return None


texts = [
    ("homework", "h"),
    ("This is an implementation", "h"),
    ("simplest", "i"),
    ("oscar", "o"),
    ("Costa Rica", "o"),
    ("duplicated", "u"),
]

for text in texts:
    result = implementation(text[0].lower())
    assert result == text[1].lower(), f"Analysing word: {text} -- Expected: {text[1]} -- Actual: {result}"

print("DONE!!")
