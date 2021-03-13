from states.State import State

class Pipe(State):

  @staticmethod
  def process(value):
    if value == '|':
      return 'LogicalOperators'
    else:
      return 'Errors'

  @classmethod
  def getType(self):
    return 'LOG'