from states.State import State

class BlockCommentAsteriskFirst(State):

  @staticmethod
  def process(value):
    if value == '*':
      return 'BlockCommentAsteriskSecond'
    else:
      return 'BlockCommentAsteriskFirst'

  @classmethod
  def getType(self):
    return 'COM'