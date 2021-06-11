"""
7. String palindrome. A palindrome is a word, phrase, number, or sequence of words that reads the same backward as forward.
"""

print("START!!\n...")


def implementation(word):
    return word == word[::-1]


test_data = [
    ("anna", True),
    ("civic", True),
    ("apple", False),
    ("level", True),
    ("hannah", True),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
