from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ExtendsT(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'e'):
      return 'ExtendsE'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'