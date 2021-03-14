from helpers.Reader import Reader
from helpers.Writer import Writer
from states.Initial import Initial
from states.Factory import Factory
from helpers.BashColors import BashColors

class StateMachine:

  @staticmethod
  def exec(inputFileName, outputFileName):
    reader = Reader(inputFileName)
    writer = Writer(outputFileName)
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
      symbol = reader.read()

      if state.isError():
        hasErrors = True

      if state.willGoToInitial(symbol) and state.isFinalState():
        if not state.ignore():
          token = state.getToken(buffer, line)
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

    reader.close()
    writer.close()