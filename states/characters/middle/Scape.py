from states.State import State
import helpers.constants as constants

class Scape(State):

  @staticmethod
  def process(value):

    if value == '"':
      return 'QuotationMarksOpen'
    elif value in constants.TO_CHARACTERS or (asciiValue >= 32 and asciiValue <=126):
      return 'QuotationMarksOpen'
    else:
      return 'ErrorsCharacters'
