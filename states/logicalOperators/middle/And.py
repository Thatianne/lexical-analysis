from states.State import State

class And(State):

  @staticmethod
  def process(value):
    if value == '&':
      return 'LogicalOperators'
    else:
      return 'ErrorsOperator'

  @classmethod
  def getType(self):
    return 'LOG'