"""
8. Verify if a word starts and ends with a consonant
"""

print("START!!\n...")


def implementation(word):
    vowels = ["a", "e", "i", "o", "u"]
    return True if word[0] not in vowels and word[-1] not in vowels else False


test_data = [
    ("anna", False),
    ("civic", True),
    ("apple", False),
    ("level", True),
    ("hannah", True),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
