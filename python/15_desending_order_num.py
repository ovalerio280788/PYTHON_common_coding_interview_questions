print("START!!\n...")


def implementation(num):
    return int("".join(sorted(list(str(num)), reverse=True)))


test_data = [
    (0, 0),
    (15, 51),
    (123456789, 987654321),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
