from helpers.Reader import Reader

reader = Reader('input/entrada2.txt')

while True:
  v = reader.read()
  if v == '"':
    reader.back()
    print(reader.read())
  print(v)
  if v == '':
    break

reader.close()