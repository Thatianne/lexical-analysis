from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralStructStringR(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'u'):
      return 'StructU'
    if (value == 'i'):
      return 'StringI'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'