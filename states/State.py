class State:

  @staticmethod
  def process(self, value):
    print("state -> process " + value)

  @staticmethod
  def isFinalState():
    return False

  @classmethod
  def getType(self):
    return self.__name__.upper()

  # throw error if isn't final state
  @classmethod
  def getToken(self, value, line):
    value = "".join(value).strip()
    token = "{:02d} ".format(line) + self.getType() + " " + value
    return token

  @staticmethod
  def willGoToInitial(value):
    return False

  @staticmethod
  def isError():
    return False

  @staticmethod
  def ignore():
    return False

  @staticmethod
  def jump(value):
    return False