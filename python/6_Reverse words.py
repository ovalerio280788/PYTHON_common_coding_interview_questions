"""
6. Reverse words. Write a method that will take a string as an argument. The method will reverse the position of words and return it.
"""

print("START!!\n...")


def implementation(words):
    words = words.split()
    words.reverse()
    return " ".join(words)


test_data = [
    ("apple banana kiwi", "kiwi banana apple"),
    ("I am Oscar Valerio", "Valerio Oscar am I"),
    ("orange", "orange"),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing array: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
