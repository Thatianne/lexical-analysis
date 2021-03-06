from states.Final import Final
from states.Initial import Initial

class Delimitators(Final):

  @staticmethod
  def process(value):
    return 'Initial'

  @staticmethod
  def willGoToInitial(value):
    return True

  @classmethod
  def getType(self):
    return 'DEL'

  @staticmethod
  def jump(value):
    return True
