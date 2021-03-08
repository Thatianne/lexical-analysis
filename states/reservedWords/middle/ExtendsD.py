from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ExtendsD(Identifiers):

  @staticmethod
  def process(value):
    if (value == 's'):
      return 'ReservedWords'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'