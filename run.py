from StateMachine import StateMachine
from os import listdir, unlink
from os.path import isfile, join

path = './output'
oldOutputs = [f for f in listdir(path) if isfile(join(path, f))]

for file in oldOutputs:
  filePath = join('output', file)
  unlink(filePath)

path = './input'
files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
  index = file[7:-4]
  StateMachine.exec('input/' + file, 'output/saida' + index + '.txt')