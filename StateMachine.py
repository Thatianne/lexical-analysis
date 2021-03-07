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
    stateName = Initial.process(symbol)
    state = Factory.get(Initial.process(symbol))
    if symbol == '\n':
        line = line + 1

    while True:
      symbol = reader.read()

      if symbol == '':
        break
      if symbol == '\n':
        line = line + 1

      if state.isFinalState() and state.willGoToInitial(symbol):
        token = state.getToken(buffer, line)
        print(token)
        writer.write(token)
        buffer.clear()

      buffer.append(symbol)
      stateName = state.process(symbol)
      state = Factory.get(stateName)

    reader.close()
    writer.close()