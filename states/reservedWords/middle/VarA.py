from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class VarA(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'r'):
      return 'ReservedWords'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'