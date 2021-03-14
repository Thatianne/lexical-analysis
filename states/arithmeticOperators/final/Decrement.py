from states.Final import Final
import helpers.constants as constants

class Decrement(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsOperator'

  @classmethod
  def getType(self):
    return 'ART'