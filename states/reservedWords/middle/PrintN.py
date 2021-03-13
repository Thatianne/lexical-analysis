from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class PrintN(Identifiers):

  @staticmethod
  def process(value):
    if (value == 't'):
      return 'ReservedWords'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'