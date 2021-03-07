from states.State import State
import helpers.constants as constants

class QuotationMarksOpen(State):

  @staticmethod
  def process(value):
    if value in constants.TO_CHARACTERS:
      return 'QuotationMarksOpen'
    elif value == '"':
      return 'Characters'
