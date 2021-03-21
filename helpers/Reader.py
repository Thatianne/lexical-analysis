class Reader:

  def __init__(self, fileName):
    self.file = open(fileName, encoding="utf-8", mode="r")
    self.position = 0

  def read(self):
    self.position = self.position + 1
    return self.file.read(1)

  def back(self):
    self.position = self.position - 1
    self.file.seek(0, 0)
    return self.file.read(self.position)

  def close(self):
    self.file.close()