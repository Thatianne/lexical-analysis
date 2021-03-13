from states.Final import Final
import helpers.constants as constants

class ErrorsCharacters(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsCharacters'

  @classmethod
  def getType(self):
    return 'CMF'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL

  @staticmethod
  def isError():
    return True