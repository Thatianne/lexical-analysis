from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class StringI(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'n'):
      return 'StringN'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'