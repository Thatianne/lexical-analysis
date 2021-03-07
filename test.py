import states

className = 'ConstN'

class_ = getattr(states, className)
print(class_)

nextClass = class_.process('s')

print(nextClass)

