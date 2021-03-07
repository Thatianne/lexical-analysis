from states.State import State
import helpers.constants as constants

class Point(State):

  @staticmethod
  def process(value):
    if value in constants.NUMBERS:
      return 'NumbersDecimal'
    else:
      from states.errors.Errors import Errors
      return 'Errors'