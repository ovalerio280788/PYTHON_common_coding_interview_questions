print("START!!\n...")


def implementation(number):
    prime_numbers = [1, 2]
    for i in range(3, number + 1):
        is_prime = True
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


test_data = [
    (12, [1, 2, 3, 5, 7, 11]),
    (20, [1, 2, 3, 5, 7, 11, 13, 17, 19]),
    (31, [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
