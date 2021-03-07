from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class TypedefEFirst(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'd'):
      return 'TypedefD'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'