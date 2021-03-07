from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralReturnRealReadR(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'e'):
      return 'GeneralReturnRealReadE'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'