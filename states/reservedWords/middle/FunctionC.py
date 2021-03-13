from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class FunctionC(Identifiers):

  @staticmethod
  def process(value):
    if (value == 't'):
      return 'FunctionT'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'