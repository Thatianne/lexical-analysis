from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class BooleanE(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'a'):
      return 'BooleanA'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'