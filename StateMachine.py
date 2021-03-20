from helpers.Reader import Reader
from helpers.Writer import Writer
from states.Initial import Initial
from states.Factory import Factory
from helpers.BashColors import BashColors
from helpers.SymbolTable import SymbolTable
import helpers.constants as constants

class StateMachine:

  @staticmethod
  def exec(inputFileName, outputFileName):
    reader = Reader(inputFileName)
    writer = Writer(outputFileName)
    symbolTable = SymbolTable()

    symbolTable.reset()
    buffer = []
    line = 1
    hasErrors = False

    print(BashColors.HEADER + inputFileName + BashColors.ENDC)
    state = Initial
    symbol = ''

    while True:
      if not state.jump(symbol):
        symbol = reader.read()
        buffer.append(symbol)
      else:
        state = Factory.get(Initial.process(symbol))

      if symbol == '\n':
        line = line + 1
      if symbol == '':
        break

      # print(state)
      # print(symbol)
      state = Factory.get(state.process(symbol))

      if state.isFinalState():
        nextSymbol = reader.read()
        reader.back()
        if state.willGoToInitial(nextSymbol):
          if not state.ignore():
            lexema = "".join(buffer).strip()
            if lexema in constants.RESERVED_WORDS:
              state = Factory.get('ReservedWords')
              token = state.getToken(buffer, line)
            else:
              token = state.getToken(buffer, line)
            if state.isError():
              print(BashColors.FAIL + token + BashColors.ENDC)
            else:
              print(BashColors.OKCYAN + token + BashColors.ENDC)
            writer.write(token)
          buffer.clear()

    if not hasErrors:
      success = 'Success!'
      writer.write(success)
      print(BashColors.OKGREEN + success + BashColors.ENDC)

    table = symbolTable.getAll()
    headers = ['Key', 'Value']
    rowFormat ="{:>10}" * (len(headers) + 1)

    print(BashColors.HEADER + '\t\tSymbol Table' + BashColors.ENDC)
    print(BashColors.OKCYAN + rowFormat.format('', *headers) + BashColors.ENDC)
    for i in range(len(table)):
      print(rowFormat.format('', *[i + 1, table[i]]))

    reader.close()
    writer.close()