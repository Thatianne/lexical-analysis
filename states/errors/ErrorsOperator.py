from states.Final import Final
import helpers.constants as constants

class ErrorsOperator(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsOperator'

  @classmethod
  def getType(self):
    return 'OpMF'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL

  @staticmethod
  def isError():
    return True