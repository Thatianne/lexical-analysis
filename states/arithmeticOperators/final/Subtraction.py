from states.Final import Final
import helpers.constants as constants

class Subtraction(Final):

  @staticmethod
  def process(value):
    if value == '-':
      return 'Decrement'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'

  @classmethod
  def getType(self):
    return 'ART'