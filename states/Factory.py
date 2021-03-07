import states

class Factory:

  @staticmethod
  def get(className):
    return getattr(states, className)
