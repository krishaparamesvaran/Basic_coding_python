string = "supreetha"
vowels = "aeiou"
count = 0

for ch in string:
    if ch in vowels:
        count = count + 1

print("The length of vowels in a given string is", count)
