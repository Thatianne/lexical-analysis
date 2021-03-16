class _Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(_Singleton('SingletonMeta', (object,), {})): pass

class SymbolTable(Singleton):
  def __init__(self):
    self.table = []

  def add(self, value):
    if value not in self.table:
      self.table.append(value)
      index = len(self.table)
    else:
      index = self.table.index(value) + 1

    return index

  def reset(self):
    self.table = []

  def getAll(self):
    return self.table

