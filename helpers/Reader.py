class Reader:

  def __init__(self, fileName):
    self.file = open(fileName, "r")
    self.position = 0

  def read(self):
    self.position = self.position + 1
    return self.file.read(1)

  def back(self):
    self.position = self.position - 1
    return self.file.seek(self.position, 0)

  def close(self):
    self.file.close()