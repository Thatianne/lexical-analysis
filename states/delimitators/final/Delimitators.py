from states.Final import Final

class Delimitators(Final):

  @staticmethod
  def process(value):
    return 'Initial'

  @classmethod
  def getType(self):
    return 'DEL'