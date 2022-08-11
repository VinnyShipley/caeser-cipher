

def encrypt(string,shift):
  encrypted = list(str(string))
  return_list = []
  for char in encrypted:
    num = ord(char)
    print(f'this is num{num}')
    big_val = num + shift
    print(f'this is big val{big_val}')
    new_key = big_val % 26
    print(f'new key {new_key}')
    new_char_val = (new_key + 97)
    new_char = chr(new_char_val)
    return_list.append(new_char)
  string = ''
  new_string = string.join(return_list)
  print(new_string)
  print(ord('b'))
  print(ord('u'))
  return new_string


def decrypt(string, key):
  pass

def crack(string):
  pass

