from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralReturnRealReadE(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'a'):
      return 'GeneralRealReadA'
    elif (value == 't'):
      return 'ReturnT'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'