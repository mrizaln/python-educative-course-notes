# Given a string, calculate the number of consonants present.

vowels = "aeiou"

# Iterative approach
def iterative_count_consonants(input_str):
    consonant_count = 0
    for char in input_str.lower():
        if char not in vowels and char.isalpha():
            consonant_count += 1
    return consonant_count

# Recursive approach
def recursive_count_consonants(input_str):
    if input_str == '': return 0

    if input_str[0] not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])

def main():
    input_str = "abc de"
    print(input_str)
    print(iterative_count_consonants(input_str))
    input_str = "LuCiDPrograMMiNG"
    print(input_str)
    print(recursive_count_consonants(input_str))

if __name__ == "__main__":
    main()