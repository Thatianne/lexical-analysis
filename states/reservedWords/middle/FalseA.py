from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class FalseA(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'l'):
      return 'FalseL'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'