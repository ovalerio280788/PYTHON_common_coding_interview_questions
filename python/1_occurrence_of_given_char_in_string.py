"""
How do you count the occurrence of a given character in a string?
"""
print("START!!\n...")


def implementation(text, char):
    return text.count(char)


texts = [
    ("homework", "o", 2),
    ("This is an implementation", "i", 4),
    ("This is an implementation", " ", 3),
    ("This is an implementation", "m", 2),
    ("", "o", 0),
]

for text in texts:
    result = implementation(text[0], text[1])
    assert result == text[2], f"Expected: {text[2]} -- Actual: {result}"

print("DONE!!")
