from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class TypedefY(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'p'):
      return 'TypedefP'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'