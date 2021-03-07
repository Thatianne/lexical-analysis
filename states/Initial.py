from states.State import State
import helpers.constants as constants

class Initial(State):

  @staticmethod
  def process(value):
    stay = [" ", "\n"]
    reservedWordsFirstLetters = ['v', 'c', 't', 's', 'e', 'p', 'f', 'r', 'i', 'w', 'b', 'g', 'l']
    # s -> struct, start, string feito
    # t -> typedef, then, true feito
    # i -> if, int feito
    # r -> return, real, read feito
    # e -> extends, else
    # p -> procedure, print
    # f -> function, false

    if value in stay:
      return 'Initial'
    elif value == 'c':
      return 'ConstC'
    elif value == 'v':
      return 'VarV'
    elif value == 't':
      return 'GeneralTypedefThenTrueT'
    elif value == 's':
      return 'GeneralStructStartStringS'
    elif value == 'i':
      return 'GeneralIfIntI'
    elif value == 'r':
      return 'GeneralReturnRealReadR'
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
