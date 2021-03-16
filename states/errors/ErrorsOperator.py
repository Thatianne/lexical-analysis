from states.errors.Errors import Errors
import helpers.constants as constants

class ErrorsOperator(Errors):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    elif value in constants.TO_DELIMITATORS:
      return 'Delimitators'
    else:
      return 'ErrorsOperator'

  @classmethod
  def getType(self):
    return 'OpMF'