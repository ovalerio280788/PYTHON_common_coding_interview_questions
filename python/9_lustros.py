"""
9. Verify how many lustros has a some years
"""

print("START!!\n...")


def implementation(data):
    return int(data / 5)


test_data = [
    (20, 4),
    (30, 6),
    (5, 1),
    (100, 20),
    (25, 5),
    (9, 1),
    (11, 2),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
