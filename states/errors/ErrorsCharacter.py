from states.Final import Final
import helpers.constants as constants

class ErrorsCharacter(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsCharacter'

  @classmethod
  def getType(self):
    return 'CMF'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL

  @staticmethod
  def isError():
    return True