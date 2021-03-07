from states.State import State

class Final(State):

  @staticmethod
  def isFinalState():
    return True

  @staticmethod
  def willGoToInitial(value):
    return True