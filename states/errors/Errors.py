from states.Final import Final
import helpers.constants as constants

class Errors(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_INITIAL:
      return 'Initial'
    elif value in constants.TO_DELIMITATORS:
      return 'Delimitators'
    else:
      return 'Errors'

  @classmethod
  def getType(self):
    return 'ERR'

  @staticmethod
  def isError():
    return True

  @staticmethod
  def jump(value):
    return value in constants.TO_DELIMITATORS