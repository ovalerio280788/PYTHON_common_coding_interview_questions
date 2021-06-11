"""
3. How is a bubble sort algorithm implemented?
"""
print("START!!\n...")


def implementation(array):
    for i in range(0, len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                # swap
                tmp = array[i]
                array[i], array[j] = array[j], tmp
    return array


test_data = [
    (
        [5, 1, 6, 2, 4, 3],
        [1, 2, 3, 4, 5, 6]
    ),
    (
        [1, 5, 6, 2, 4, 3],
        [1, 2, 3, 4, 5, 6]
    ),
    (
        [5, 8, 9, 7, 45, 87, 96],
        [5, 7, 8, 9, 45, 87, 96]
    ),
    (
        [20, 15, 22, 11, 15, 21, 7],
        [7, 11, 15, 15, 20, 21, 22]
    ),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing array: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
