from states.Final import Final

class LogicalOperators(Final):

  @staticmethod
  def process(value):
    if value == '=':
      return 'RelationalOperatorsEquals'
    else:
      return 'Initial'

  @classmethod
  def getType(self):
    return 'LOG'