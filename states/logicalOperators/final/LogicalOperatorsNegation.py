from states.Final import Final

class LogicalOperatorsNegation(Final):

  @staticmethod
  def process(value):
    if value == '=':
      return 'RelationalOperatorsEquals'
    else:
      return 'Initial'

  @classmethod
  def getType(self):
    return 'LOG'

  @staticmethod
  def willGoToInitial(value):
    return value != '='