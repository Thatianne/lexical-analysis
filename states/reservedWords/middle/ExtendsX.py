from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ExtendsX(Identifiers):

  @staticmethod
  def process(value):
    if (value == 't'):
      return 'ExtendsT'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'