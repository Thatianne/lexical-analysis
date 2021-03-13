from helpers.Reader import Reader
from helpers.Writer import Writer
from states.Initial import Initial
from states.Factory import Factory

class StateMachine:

  @staticmethod
  def exec(inputFileName, outputFileName):
    reader = Reader(inputFileName)
    writer = Writer(outputFileName)
    buffer = []
    line = 1

    symbol = reader.read()
    buffer.append(symbol)
    state = Factory.get(Initial.process(symbol))

    if symbol == '\n':
        line = line + 1

    while True:
      # print(state)
      # print(symbol)
      symbol = reader.read()

      if state.willGoToInitial(symbol):
        token = ''
        if state.isError():
          token = state.getToken(buffer, line)
        elif state.isFinalState():
          token = state.getToken(buffer, line)
        print(token)
        writer.write(token)
        buffer.clear()

      buffer.append(symbol)
      state = Factory.get(state.process(symbol))

      if symbol == '':
        break
      if symbol == '\n':
        line = line + 1

    reader.close()
    writer.close()