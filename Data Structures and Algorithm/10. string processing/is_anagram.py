# Simply put, an anagram is when two strings can be written using the same letters.

# examples:
    # "rail safety" = "fairy tales"
    # "roast beef" = "eat for BSE"

s1 = "fairy tales"
s2 = "rail safety"

# normalizing strings
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# time complexity: O(nlogn) [cause sorting is O(nlogn)]
print(sorted(s1) == sorted(s2))

# time complexity: O(n)
# but space?
def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 0

    for i in ht:
        if ht[i] != 0:
            return False

    return True

print(is_anagram(s1, s2))