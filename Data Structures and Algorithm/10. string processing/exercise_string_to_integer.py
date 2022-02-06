# Given some numeric string as input, convert the string to an integer.

def str_to_int(input_str):
    if input_str[0] == "-":
        is_negative = True
        input_str = input_str[1:]
    else:
        is_negative = False

    output_int = 0
    for i in input_str:
        output_int *= 10
        output_int += ord(i) - ord('0')

    if is_negative:
        return output_int * -1
    else:
        return output_int


print(str_to_int("121"))
print(str_to_int("-1293"))
print(str_to_int("-999"))
print(str_to_int("0"))
