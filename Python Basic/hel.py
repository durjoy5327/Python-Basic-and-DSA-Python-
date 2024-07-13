import json

# Using a raw string to avoid escape sequence issues
with open(r"F:\python practice\info.txt", "r") as f:
    k = f.read()

book = json.loads(k)
print(book)
