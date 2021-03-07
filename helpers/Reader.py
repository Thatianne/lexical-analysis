class Reader:

  def __init__(self, fileName):
    self.file = open(fileName, "r")

  def read(self):
    return self.file.read(1)

  def close(self):
    self.file.close()