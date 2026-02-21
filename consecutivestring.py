s = "999999"

max_count = 1
count = 1
char = s[0]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
        if count > max_count:
            max_count = count
            char = s[i]
    else:
        count = 1

print("The letter", char, "occurs", max_count, "times consecutively")
