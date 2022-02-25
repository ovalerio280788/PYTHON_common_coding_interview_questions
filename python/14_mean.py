print("START!!\n...")


def implementation(marks):
    return sum(marks) // len(marks)


test_data = [
    ([2, 5, 9, 50, 6, 45], 19),
    ([12, 5, 19, 5, 6, 5], 8),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
