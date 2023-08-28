words = ["hello", "my", "name", "is", "Sam"]
result = [(lambda word: (word.upper(), len(word))) (word) for word in words]
print(result)