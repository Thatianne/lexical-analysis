from states.Final import Final
import helpers.constants as constants

class ErrorsNumber(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsNumber'

  @classmethod
  def getType(self):
    return 'NMF'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL

  @staticmethod
  def isError():
    return True