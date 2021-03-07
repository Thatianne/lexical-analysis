from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class TypedefD(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'e'):
      return 'TypedefESecond'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'