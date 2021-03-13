from states.Final import Final

class BlockComment(Final):

  @staticmethod
  def process(value):
    return 'Initial'

  @classmethod
  def getType(self):
    return 'COM'

  @staticmethod
  def ignore():
    return True