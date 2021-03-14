from states.Final import Final
import helpers.constants as constants

class ReservedWords(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    elif value in constants.TO_DELIMITATORS:
      return 'Delimitators'
    elif value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    else:
      return 'Errors'

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL or value in constants.TO_DELIMITATORS

  @classmethod
  def getType(self):
    return 'PRE'
