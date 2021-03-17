from states.errors.Errors import Errors
import helpers.constants as constants

class ErrorsCharacter(Errors):

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
  def jump(value):
    return value in constants.TO_DELIMITATORS