from states.Final import Final
import helpers.constants as constants

class ErrorsComment(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsComment'

  @classmethod
  def getType(self):
    return 'CoMF'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL

  @staticmethod
  def isError():
    return True