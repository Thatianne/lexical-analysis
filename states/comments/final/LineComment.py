from states.Final import Final

class LineComment(Final):

  @staticmethod
  def process(value):
    if value == '\n':
      return 'Initial'
    else:
      return 'LineComment'

  @staticmethod
  def willGoToInitial(value):
    return value == '\n'

  @classmethod
  def getType(self):
    return 'COM'

  @staticmethod
  def ignore():
    return True