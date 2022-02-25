import re
import string

print("START!!\n...")


def implementation(data):
    return sorted(set(string.ascii_lowercase)) <= sorted(set(re.findall("[a-z]", data.lower())))


test_data = [
    ("Mr. Jock, TV quiz PhD., bags few lynx.", True),
    ("GQ's oft lucky whiz Dr. J, ex-NBA MVP - Steve Galen", True),
    ("GQ's oft lucky whia Dr. J, ex-NBA MVP - Steve Glen", False),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
