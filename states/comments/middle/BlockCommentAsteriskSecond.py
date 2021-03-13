from states.State import State

class BlockCommentAsteriskSecond(State):

  @staticmethod
  def process(value):
    if value == '/':
      return 'BlockComment'
    else:
      return 'Errors'

  @classmethod
  def getType(self):
    return 'COM'