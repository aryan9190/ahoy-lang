import re
from utils import ParseError

COMMAND_PATTERNS = [
    (re.compile(r"^Add (\d+) to the booty!$", re.IGNORECASE), lambda m: ('ADD', int(m.group(1)))),
    (re.compile(r"^Subtract (\d+) from the booty!$", re.IGNORECASE), lambda m: ('SUB', int(m.group(1)))),
    (re.compile(r"^Multiply booty by (\d+)!$", re.IGNORECASE), lambda m: ('MULTIPLY', int(m.group(1)))),
    (re.compile(r"^Divide booty in (\d+) pieces!$", re.IGNORECASE), lambda m: ('DIVIDE', int(m.group(1)))),
    (re.compile(r"^Fire the cannon!$", re.IGNORECASE), lambda m: ('FETCH', None)),
    (re.compile(r"^Stash the booty!$", re.IGNORECASE), lambda m: ('PUSH', None)),
    (re.compile(r"^Grab from the barrel!$", re.IGNORECASE), lambda m: ('POP', None)),
    (re.compile(r"^Name the booty ([a-zA-Z_][a-zA-Z0-9_]*)!$", re.IGNORECASE), lambda m: ('STORE', m.group(1))),
    (re.compile(r"^Call upon ([a-zA-Z_][a-zA-Z0-9_]*)!$", re.IGNORECASE), lambda m: ('CALL', m.group(1))),
    (re.compile(r"^Ask for ([a-zA-Z_][a-zA-Z0-9_]*) from the ledger!$", re.IGNORECASE), lambda m: ('LOAD', m.group(1))),
    (re.compile(r"^Set sail if the booty be no 0!$", re.IGNORECASE), lambda m: ('LOOP_START', None)),
    (re.compile(r"^Drop Anchor!$", re.IGNORECASE), lambda m: ('LOOP_END', None)),
    (re.compile(r"^Drink rum!$", re.IGNORECASE), lambda m: ('RUM', None)),
    (re.compile(r"^Swab the deck!$", re.IGNORECASE), lambda m: ('SWAB', None)),
    (re.compile(r"^Parrot says (.+)!$", re.IGNORECASE), lambda m: ('PRINT', m.group(1))),
    (re.compile(r"^Echo from the parrot!$", re.IGNORECASE), lambda m: ('INPUT', None)),
    (re.compile(r"^Walk the plank!$", re.IGNORECASE), lambda m: ('EXIT', None)),
]

SYMBOL_MAP = {
    '+': ('ADD', 1),
    '-': ('SUB', 1),
    '*': ('MULTIPLY', 1),
    '/': ('DIVIDE', 1),
    '`': ('FETCH', None),
    '$': ('PUSH', None),
    '%': ('INPUT', None),
    '^': ('POP', None),
    '[': ('LOOP_START', None),
    ']': ('LOOP_END', None),
    '!': ('EXIT', None),
    '~': ('RUM', None)
}

def parse(file_path: str):
    with open(file_path) as f:
        raw_lines = f.readlines()

    lines = [l.split('#')[0].strip() for l in raw_lines if l.strip() and not l.strip().startswith('#')]

    if not lines:
        return [], {}

    first = lines[0]
    mode = 'MAP' if all(ch in SYMBOL_MAP for ch in first) else 'PIRATE'

    instructions = []
    functions = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r"^Raise the sails ye scallywag ([a-zA-Z_][a-zA-Z0-9_]*)!$", line, re.IGNORECASE)
        if match:
            name = match.group(1)
            func_body = []
            i += 1
            while i < len(lines) and not re.match(r"^Lower the sails!$", lines[i], re.IGNORECASE):
                func_body.append(lines[i])
                i += 1
            functions[name] = func_body
            i += 1  # skip 'Lower the sails!'
            continue

        matched = False
        for pattern, action in COMMAND_PATTERNS:
            m = pattern.match(line)
            if m:
                instructions.append(action(m))
                matched = True
                break
        if not matched:
            raise ParseError(f"Blimey! Couldn't understand: {line}")
        i += 1

    return instructions, functions
