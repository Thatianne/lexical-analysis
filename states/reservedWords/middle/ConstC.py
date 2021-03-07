from states.identifiers.final.Identifiers import Identifiers
# from states.State import State
import helpers.constants as constants

class ConstC(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'o'):
      return 'ConstO'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'