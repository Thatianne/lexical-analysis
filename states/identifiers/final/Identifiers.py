from states.Final import Final
import helpers.constants as constants

class Identifiers(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL

  @classmethod
  def getType(self):
    return 'IDE'
