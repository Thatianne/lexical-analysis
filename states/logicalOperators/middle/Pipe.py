from states.State import State

class Pipe(State):

  @staticmethod
  def process(value):
    if value == '|':
      return 'LogicalOperators'
    else:
      return 'ErrorsOperator'

  @classmethod
  def getType(self):
    return 'LOG'