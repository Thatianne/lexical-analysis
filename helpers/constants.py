import string

NUMBERS = list(string.digits)
LETTERS = list(string.ascii_letters)

TO_IDENTIFIERS = LETTERS + NUMBERS + ['_']
TO_CHARACTERS = LETTERS + NUMBERS
TO_RELATIONAL_OPS = ['=', '>', '<']
TO_INITIAL = [' ', '', '\n', '\t', '\r']
TO_DELIMITATORS = [';', ',', '(', ')', '{', '}', '[', ']', '.']
RESERVED_WORDS = ['var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start', 'return', 'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean', 'string', 'true', 'false', 'global', 'local']
