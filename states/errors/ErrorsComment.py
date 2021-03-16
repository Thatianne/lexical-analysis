from states.errors.Errors import Errors
import helpers.constants as constants

class ErrorsComment(Errors):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    elif value in constants.TO_DELIMITATORS:
      return 'Delimitators'
    else:
      return 'ErrorsComment'

  @classmethod
  def getType(self):
    return 'CoMF'