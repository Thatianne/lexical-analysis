class Writer:

  def __init__(self, fileName):
    self.file = open(fileName, "w")

  def write(self, value):
    self.file.write(value + "\n")

  def close(self):
    self.file.close()