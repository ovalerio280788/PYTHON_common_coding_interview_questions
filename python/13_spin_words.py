print("START!!\n...")


def implementation(sentence):
    return " ".join(
        [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    )


test_data = [
    ("Welcome", "emocleW"),
    ("to", "to"),
    ("This sentence is a sentence", "This ecnetnes is a ecnetnes"),
    ("Hey fellow warriors", "Hey wollef sroirraw")
]

for data in test_data:
    result = implementation(data[0])
    assert result == data[1], f"Analysing: {data[0]} -- Expected: {data[1]} -- Actual: {result}"

print("DONE!!")
