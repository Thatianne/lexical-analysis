from states.Final import Final
import helpers.constants as constants

class NumbersFloat(Final):

  @staticmethod
  def process(value):
    if value in constants.NUMBERS:
      return 'NumbersFloat'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsNumber'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL or (value in constants.TO_DELIMITATORS and value != '.')

  @classmethod
  def getType(self):
    return 'NRO'