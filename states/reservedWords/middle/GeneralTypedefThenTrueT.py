from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralTypedefThenTrueT(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'y'):
      return 'TypedefY'
    elif value == 'h':
      return 'ThenH'
    elif value == 'r':
      return 'TrueR'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'