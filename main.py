from itertools import cycle

punctuation_cycle = cycle(['!', '.'])

letterdict = {}

with open("books/frankenstein.txt") as f:
    content = f.read()
    for char in content:
        print(char)
        if char.isalpha() is False:
            continue
        if char.lower() not in letterdict:
            letterdict[char.lower()] = 1
        else:
            letterdict[char.lower()] += 1

letterdict = dict(sorted(letterdict.items(), key=lambda x: x[1], reverse=True))
print(letterdict)

print("Total letter count: ", sum(letterdict.values()))
print("---------Letter summary----------")
for key, value in letterdict.items():
    # Add the next character from the cycle to the end of the string
    print(f"{key} appeared {value} times{next(punctuation_cycle)}")
print("---------End----------")
