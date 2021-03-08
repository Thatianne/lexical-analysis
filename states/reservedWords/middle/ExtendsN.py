from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ExtendsN(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'd'):
      return 'ExtendsD'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'