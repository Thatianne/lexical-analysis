from states.errors.Errors import Errors
import helpers.constants as constants

class ErrorsCharacter(Errors):

  @staticmethod
  def process(value):
    return 'Initial'
    # if value in constants.TO_INITIAL:
    # else:
    #   return 'ErrorsCharacter'

  @classmethod
  def getType(self):
    return 'CMF'

  @staticmethod
  def jump(value):
    return True

  @staticmethod
  def willGoToInitial(value):
    return True