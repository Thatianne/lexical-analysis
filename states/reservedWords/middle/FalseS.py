from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class FalseS(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'e'):
      return 'ReservedWords'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'