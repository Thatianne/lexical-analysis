from states.Final import Final
import helpers.constants as constants

class Division(Final):

  @staticmethod
  def process(value):
    if value == '/':
      return 'LineComment'
    elif value == '*':
      return 'BlockCommentAsteriskFirst'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'ErrorsOperator'

  @classmethod
  def getType(self):
    return 'ART'