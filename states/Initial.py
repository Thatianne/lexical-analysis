from states.State import State
import helpers.constants as constants

class Initial(State):

  @staticmethod
  def process(value):
    stay = [" ", "\n"]
    reservedWordsFirstLetters = ['v', 'c', 't', 's', 'e', 'p', 'f', 'r', 'i', 'w', 'b', 'g', 'l']
    # s -> struct, start,
    # e -> extends, else
    # t -> typedef, then, true feito
    # r -> return, read,
    # p -> procedure, print
    # i -> if, int
    # r -> return, real
    # s -> start, string
    # f -> function, false

    if value in stay:
      return 'Initial'
    elif value == 'c':
      return 'ConstC'
    elif value == 'v':
      return 'VarV'
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
    else:
      return 'Errors'
