from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class FunctionN(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'c'):
      return 'FunctionC'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'