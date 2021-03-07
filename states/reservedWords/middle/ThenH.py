from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ThenH(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'e'):
      return 'ThenE'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'