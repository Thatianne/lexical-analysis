from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralRealReadA(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'd' or value == 'l'):
      return 'ReservedWords'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'