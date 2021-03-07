from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralIfIntI(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'f'):
      return 'ReservedWords'
    elif value == 'n':
      return 'IntN'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'