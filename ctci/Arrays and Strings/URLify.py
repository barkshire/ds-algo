def urlify(string, length):
  new_index = len(string)
  new_string = ''
  string_iterator = list(string)
  for i in reversed(range(length)):
    if string[i] == ' ':
      string_iterator[new_index-3:new_index] = '%20'
      new_index -= 3
    else:
      string_iterator[new_index-1] = string[i]
      new_index -= 1
  return new_string.join(string_iterator)

testcase = 'Mr John Smith    '
size = 13

print(urlify(testcase, size))
