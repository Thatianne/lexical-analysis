from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralProcedurePrintR(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'i'):
      return 'PrintI'
    elif value == 'o':
      return 'ProcedureO'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'