from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class ProcedureEFirst(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'd'):
      return 'ProcedureD'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'