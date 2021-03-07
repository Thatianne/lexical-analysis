from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ConstO(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'n'):
      return 'ConstN'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'