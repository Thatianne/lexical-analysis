from states.State import State
import helpers.constants as constants

class QuotationMarksOpen(State):

  @staticmethod
  def process(value):
    asciiValue = 0
    if value != '':
      asciiValue = ord(value)

    if value == '"':
      return 'Characters'
    elif value == '\\':
      return 'Scape'
    elif value in constants.TO_CHARACTERS or (asciiValue >= 32 and asciiValue <=126):
      return 'QuotationMarksOpen'
    elif value == '\n' or value == '':
      return 'ErrorsCharacters'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsCharacters'
