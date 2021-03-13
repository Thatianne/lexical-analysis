from states.State import State
import helpers.constants as constants

class Final(State):

  @staticmethod
  def isFinalState():
    return True

  @staticmethod
  def willGoToInitial(value):
    return value in constants.TO_INITIAL
