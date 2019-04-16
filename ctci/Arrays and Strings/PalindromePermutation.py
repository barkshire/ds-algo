def per_pal(str):
  table = [0 for _ in range(ord('z')-ord('a')+1)]

  countodd = 0

  for c in str:
    x = char_num(c)
    if x != -1:
      table[x] += 1
      if table[x]%2:
        countodd += 1
      else:
        countodd -= 1
  return countodd <= 1



def char_num(c):
  a = ord('a')
  z = ord('z')
  A = ord('A')
  Z = ord('Z')
  val = ord(c)

  if a <= val <= z:
    return val - a
  elif A <= val <= Z:
    return val - A
  return -1 


print(per_pal('Tact Coa'))
print(per_pal('So patient a nurse to nurse a patient so'))
print(per_pal('Not a Palindrome'))
