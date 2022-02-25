print("START!!\n...")


def implementation(data):
    if len(data) == 1:
        return data[0]

        # sort date
    sorted_data = sorted(data)
    print(sorted_data)

    # define middle
    middle = (len(sorted_data) - 1) // 2
    print(f"Middle: {middle}")
    print(f"Even number?: {len(sorted_data) % 2 == 0}")

    if len(sorted_data) % 2 == 0:
        # even number of elements
        return (sorted_data[middle] + sorted_data[middle + 1]) / 2.0
    else:
        # odd number of elements
        return sorted_data[middle]


test_data = [
    ([3, 2, 1], 2),
    ([1], 1),
    ([1234, 345, 78], 345),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
