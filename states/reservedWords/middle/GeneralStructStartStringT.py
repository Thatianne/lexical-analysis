from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralStructStartStringT(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'r'):
      return 'GeneralStructStringR'
    elif (value == 'a'):
      return 'StartA'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'