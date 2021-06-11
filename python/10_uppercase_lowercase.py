"""
10. take a word and if a character is in lowercase then convert to uppercase, and vice versa
"""

print("START!!\n...")


def implementation(data):
    return "".join([char.upper() if char.islower() else char.lower() for char in list(data)])


test_data = [
    ("HoLa", "hOlA"),
    ("coSTa rIcA", "COstA RiCa"),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
