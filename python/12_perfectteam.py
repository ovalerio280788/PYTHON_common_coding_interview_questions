print("START!!\n...")


def implementation(skills):
    perfect_team = ['p', 'c', 'm', 'b', 'z']
    return min([list(skills).count(x) for x in perfect_team])


test_data = [
    ("pcmbzpcmbz", 2),
    ("mppzbmbpzcbmpbmczcz", 3),
    ("pcmbzpcmbzpcmbzpcmbz", 4),
    ("pcmbzpcmbzpcmbzpcmbzpcm", 4),
    ("oscar", 0),
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
