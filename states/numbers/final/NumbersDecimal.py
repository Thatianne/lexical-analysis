from states.Final import Final
import helpers.constants as constants

class NumbersDecimal(Final):

  @staticmethod
  def process(value):
    if value in constants.NUMBERS:
      return 'NumbersDecimal'
    elif value == '.':
      return 'Point'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'

  @staticmethod
  def willGoToInitial(value):
    return value not in constants.NUMBERS

  @classmethod
  def getType(self):
    return 'NRO'