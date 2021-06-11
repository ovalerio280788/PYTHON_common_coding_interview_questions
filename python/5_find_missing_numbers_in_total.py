"""
4. How do you remove duplicates from an array in place?
"""

print("START!!\n...")


def implementation(array, total_max_number):
    missing_numbers = []
    for i in range(1, total_max_number + 1):
        if array.count(i) == 0:
            missing_numbers.append(i)
    return missing_numbers


test_data = [
    # entry array,   max/total numbers,     expected missing numbers as an array
    ([1, 2, 3, 4, 6], 6, [5]),
    ([1, 2, 3, 4, 6, 7, 9, 8, 10], 10, [5]),
    ([1, 2, 3, 4, 6, 9, 8], 10, [5, 7, 10]),
    ([1, 2, 3, 4, 9, 8], 10, [5, 6, 7, 10]),
]

for data in test_data:
    result = implementation(data[0], data[1])
    assert result == data[2], f"Analysing array: {data[0]} -- Expected: {data[2]} -- Actual: {result}"

print("DONE!!")
