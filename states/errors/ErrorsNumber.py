from states.State import State
import helpers.constants as constants

class ErrorsNumber(State):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'

  @classmethod
  def getType(self):
    return 'NMF'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL

  @staticmethod
  def isError():
    return True