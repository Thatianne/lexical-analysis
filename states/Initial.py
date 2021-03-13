from states.State import State
import helpers.constants as constants

class Initial(State):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
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
    elif value == 'e':
      return 'GeneralExtendsElseE'
    elif value == 'f':
      return 'GeneralFunctionFalseF'
    elif value == 'p':
      return 'GeneralProcedurePrintP'
    elif value == 'w':
      return 'WhileW'
    elif value == 'b':
      return 'BooleanB'
    elif value == 'g':
      return 'GlobalG'
    elif value == 'l':
      return 'LocalL'
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
