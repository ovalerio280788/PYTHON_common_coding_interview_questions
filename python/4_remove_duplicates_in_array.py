"""
4. How do you remove duplicates from an array in place?
"""
print("START!!\n...")


def implementation(array):
    return list(dict.fromkeys(array))


texts = [
    ([1, 1, 2, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 1, 2, 3, 4, 5, 2, 2, 1, 1], [1, 2, 3, 4, 5]),
    (["test1", "test2", "test1", "test2", "test1", "test3"], ["test1", "test2", "test3"]),
]

for text in texts:
    result = implementation(text[0])
    assert result == text[1], f"Analysing word: {text} -- Expected: {text[1]} -- Actual: {result}"

print("DONE!!")
