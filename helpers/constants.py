import string

NUMBERS = list(string.digits)
LETTERS = list(string.ascii_letters)

TO_IDENTIFIERS = LETTERS + NUMBERS + ['_']
TO_CHARACTERS = LETTERS + NUMBERS
TO_RELATIONAL_OPS = ['=', '>', '<']
TO_INITIAL = [' ', '\n', '']
TO_DELIMITATORS = [';', ',', '(', ')', '{', '}', '[', ']', '.']
