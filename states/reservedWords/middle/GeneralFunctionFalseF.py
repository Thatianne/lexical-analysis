from states.identifiers.final.Identifiers import Identifiers
import helpers.constants as constants

class GeneralFunctionFalseF(Identifiers):

  @staticmethod
  def process(value):
    if (value == 'u'):
      return 'FunctionU'
    elif (value == 'a'):
      return 'FalseA'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'