# In this lesson, we will be considering the so-called “Look-and-Say” sequence. The first few terms of the sequence are:

    # 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

# To generate a member of the sequence from the previous member, read off the digits of the previous member
# and record the count of the number of digits in groups of the same digit.

def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(f"{count}{s[i]}")
        i += 1
    return ''.join(result)

sequence = "1"
print(sequence)

for i in range(10):
    sequence = next_number(sequence)
    print(sequence)