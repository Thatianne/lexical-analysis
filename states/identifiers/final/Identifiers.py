from states.Final import Final
import helpers.constants as constants
from helpers.SymbolTable import SymbolTable
symbolTable = SymbolTable()

class Identifiers(Final):

  @staticmethod
  def process(value):
    if value in constants.TO_IDENTIFIERS:
      return 'Identifiers'
    elif value in constants.TO_INITIAL:
      return 'Initial'
    else:
      return 'Errors'

  @classmethod
  def getType(self):
    return 'IDE'

  @classmethod
  def getToken(self, value, line):
    value = "".join(value).strip()
    index = symbolTable.add(value)
    token = "{:02d} ".format(line) + self.getType() + " " + str(index)
    return token
