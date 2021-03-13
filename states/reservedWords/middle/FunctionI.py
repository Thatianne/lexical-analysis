from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class FunctionI(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'o'):
      return 'FunctionO'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'