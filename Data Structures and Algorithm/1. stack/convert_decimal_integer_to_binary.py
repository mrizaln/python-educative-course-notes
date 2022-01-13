from the_stack import Stack

def convert_int_to_bin(dec_num):
  bin_stack = Stack()

  if dec_num == 0: return 0

  while dec_num != 0:
    mod = dec_num % 2
    dec_num = dec_num // 2
    bin_stack.push(mod)
  
  the_bin = ""
  
  while not bin_stack.is_empty():
    the_bin += str(bin_stack.pop())
  
  return the_bin

if __name__ == "__main__":
    num = 0
    print(num)
    num = convert_int_to_bin(num)
    print(num)