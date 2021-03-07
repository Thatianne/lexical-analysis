from states.Final import Final
import helpers.constants as constants

class NumbersFloat(Final):

  @staticmethod
  def process(value):
    if value in constants.NUMBERS:
      return 'NumbersFloat'
    elif value == constants.TO_INITIAL:
      return 'Initial'

  @staticmethod
  def willGoToInitial(value):
    return value not in constants.NUMBERS

  @classmethod
  def getType(self):
    return 'NRO'