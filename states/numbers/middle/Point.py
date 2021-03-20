from states.State import State
import helpers.constants as constants

class Point(State):

  @staticmethod
  def process(value):
    if value in constants.NUMBERS:
      return 'NumbersFloat'
    else:
      return 'ErrorsNumber'

  @staticmethod
  def jump(value):
    return value in constants.TO_DELIMITATORS and value != '.'