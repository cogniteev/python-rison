import re


WHITESPACE = ''

IDCHAR_PUNCTUATION = '_-./~'

NOT_IDCHAR = " '!:(),*@$"

# Additionally, we need to distinguish ids and numbers by first char.
NOT_IDSTART = '-0123456789'

# Regexp string matching a valid id.
IDRX = ('[^' + NOT_IDSTART + NOT_IDCHAR + '][^' + NOT_IDCHAR + ']*')

# Regexp to check for valid rison ids.
ID_OK_RE = re.compile('^' + IDRX + '$', re.M)

# Regexp to find the end of an id when parsing.
NEXT_ID_RE = re.compile(IDRX, re.M)
