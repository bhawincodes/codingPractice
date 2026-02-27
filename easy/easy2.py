# https://www.hackerearth.com/community/practice/palindrome-split-efe4c78a/

# here the max palindromes we can create is by taking the pairs of 2


t = int(input())
for i in range(t):
    characters = {}
    s = input()
    for c in s:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    count = 0
    # iterate on each key in characters
    for key in characters.keys():
        count += int(characters[key] / 2)

    print(count)
