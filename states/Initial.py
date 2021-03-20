from states.State import State
import helpers.constants as constants

class Initial(State):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    elif value == '&':
      return 'And'
    elif value == '|':
      return 'Pipe'
    elif value == '+':
      return 'Sum'
    elif value == '-':
      return 'Subtraction'
    elif value == '/':
      return 'Division'
    elif value == '*':
      return 'Multiplication'
    elif value in constants.LETTERS:
      return 'Identifiers'
    elif value in constants.NUMBERS:
      return 'NumbersDecimal'
    elif value == '"':
      return 'QuotationMarksOpen'
    elif value == '!':
      return 'LogicalOperatorsNegation'
    elif value in constants.TO_RELATIONAL_OPS:
      return 'RelationalOperators'
    elif value in constants.TO_DELIMITATORS:
      return 'Delimitators'
    else:
      return 'Errors'
