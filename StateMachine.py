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
    line = 0

    symbol = reader.read()
    buffer.append(symbol)
    state = Factory.get(Initial.process(symbol))

    if symbol == '\n':
        line = line + 1

    while True:
      symbol = reader.read()

      if symbol == '\n':
        line = line + 1

      if state.isFinalState() and state.willGoToInitial(symbol):
        token = state.getToken(buffer, line)
        print(token)
        writer.write(token)
        buffer.clear()

      buffer.append(symbol)
      state = Factory.get(state.process(symbol))

      if symbol == '':
        break

    reader.close()
    writer.close()