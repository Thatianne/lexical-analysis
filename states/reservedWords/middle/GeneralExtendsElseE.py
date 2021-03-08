from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralExtendsElseE(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'l'):
      return 'ElseL'
    if (value == 'x'):
      return 'ExtendsX'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'