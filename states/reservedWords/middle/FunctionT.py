from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class FunctionT(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'i'):
      return 'FunctionI'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'