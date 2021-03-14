from states.Final import Final
import helpers.constants as constants

class Characters(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    elif value in constants.TO_DELIMITATORS:
      return 'Delimitators'
    else:
      return 'Errors'

  @classmethod
  def getType(self):
    return 'CAD'