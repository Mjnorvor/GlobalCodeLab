sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
new = [len(word) for word in words if word != "the"]
print(new)