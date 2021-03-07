from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ReturnT(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'u'):
      return 'ReturnU'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'