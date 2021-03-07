from states.Final import Final

class RelationalOperatorsEquals(Final):

  @staticmethod
  def process(value):
    return 'Initial'

  @classmethod
  def getType(self):
    return 'REL'