from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralProcedurePrintP(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'r'):
      return 'GeneralProcedurePrintR'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'