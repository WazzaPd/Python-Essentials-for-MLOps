# Implement a phone book as a dictionary.
entry = {
    "name": "Joseph Wu",
    "address": "This is an address",
    "number": "111-123-1234"
}

phoneBook = {}

for i in range(3):
    phoneBook[i] = entry

print(phoneBook)


# Find the most frequent words in a text file using sets
text = "This is to simuplate a text file. Let's see what the most frequent word is in this file"
words = list(text.split(" "))
uniqueWords = set()
count = {}
for i in words:
    uniqueWords.add(i)
for i in uniqueWords:
    count[i] = 0

for i in words:
    for key in count.keys():
        if i == key:
            count[key] += 1

largestWord = ""
largest = 0
for i in count:
    if count[i] > largest:
        largest = count[i]
        largestWord = i
print(f"\nThis is the most frequent word: {largestWord}")

# Filter user-submitted comments stored in a list for profanity
comments = [
    "This is cool",
    "Your mom",
    "Profanity1",
    "Hi",
    "Profanity2"
]
bannedWords = [
    "Profanity1",
    "Profanity2",
    "Profanity3"
]
for i in comments:
    for ban in bannedWords:
        if i == ban:
            comments.remove(ban)
print(f"Clean comments: {comments}")

# Build a historgram from word counts using dictionaries
print("\nHistogram: ")
for i in count.keys():
    print(f"{i}: {'#' * count[i]}")

# Convert a deeply nested list into a flat list
nested = ["hi", ["I", ["like", ["to", ["write", ["Hello world!"]]]]]]
flat = []
def flatten(nested):
    for item in nested:
        if type(item) == list:
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return []
flatten(nested)
print(f"\nflat list: {flat}")