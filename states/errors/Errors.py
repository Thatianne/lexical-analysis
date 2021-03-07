from states.State import State

class Errors(State):

  @staticmethod
  def process(value):
    from states.Initial import Initial
    return 'Initial'