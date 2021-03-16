from states.errors.Errors import Errors
import helpers.constants as constants

class ErrorsNumber(Errors):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    elif value in constants.TO_DELIMITATORS:
      return 'Delimitators'
    else:
      return 'ErrorsNumber'

  @classmethod
  def getType(self):
    return 'NMF'

  @staticmethod
  def jump(value):
    return value in constants.TO_DELIMITATORS and value != '.'