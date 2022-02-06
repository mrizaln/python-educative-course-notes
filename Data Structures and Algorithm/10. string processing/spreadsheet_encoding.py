# In this lesson, we will be considering how to solve the problem of implementing a function that
# converts a spreadsheet column ID (i.e., “A”, “B”, “C”, …, “Z”, “AA”, etc.) to the corresponding
# integer. For example, “A” equals 1 because it represents the first column, while “AA” equals 27
# because it represents the 27th column.

# Python ord() function
    # returns an integer which represents the unicode cod pint of the char
print(ord("A"))
print(ord("B"))
print(ord("C"))
print(ord("D"))

# Algorithm:
    # treat alphabet as 26 base numbering system
# A  = 1
# Z  = 26
# AA = 27

# first step: translate the 26 alphabet to 26 base number
print("A =", ord("A") - ord("A") + 1)
print("B =", ord("B") - ord("A") + 1)
print("F =", ord("F") - ord("A") + 1)
print("Z =", ord("Z") - ord("A") + 1)
print()

# Implementation
def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str) - 1
    for s in col_str:
        num += 26**count *(ord(s) - ord('A') + 1)
        count -= 1
    return num

col = 'ZZ'
print(f"{col} = {spreadsheet_encode_column('ZZ')}")