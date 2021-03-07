from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class TrueR(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'u'):
      return 'TrueU'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'