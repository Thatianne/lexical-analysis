from helpers.Reader import Reader
from helpers.Writer import Writer
from states.Initial import Initial
from states.Factory import Factory
from helpers.BashColors import BashColors
from helpers.SymbolTable import SymbolTable

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
    symbol = reader.read()
    buffer.append(symbol)
    state = Factory.get(Initial.process(symbol))

    if symbol == '\n':
        line = line + 1

    while True:
      # print(state)
      # print(symbol)
      if not state.jump(symbol):
          symbol = reader.read()

      if state.isError():
        hasErrors = True

      if state.willGoToInitial(symbol) and state.isFinalState():
        if not state.ignore():
          token = state.getToken(buffer, line)
          if not state.jump(symbol):
            if state.isError():
              print(BashColors.FAIL + token + BashColors.ENDC)
            else:
              print(BashColors.OKCYAN + token + BashColors.ENDC)
            writer.write(token)
        buffer.clear()

      buffer.append(symbol)
      state = Factory.get(state.process(symbol))

      if symbol == '' and not state.isFinalState():
        break
      if symbol == '\n':
        line = line + 1

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