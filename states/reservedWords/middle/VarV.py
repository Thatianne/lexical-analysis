from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class VarV(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'a'):
      return 'VarA'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'