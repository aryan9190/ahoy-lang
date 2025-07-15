import random
from parser import parse
from utils import ParseError

def find_matching_end(start, instrs):
    depth = 1
    for i in range(start+1, len(instrs)):
        cmd, _ = instrs[i]
        if cmd == 'LOOP_START':
            depth += 1
        elif cmd == 'LOOP_END':
            depth -= 1
        if depth == 0:
            return i
    raise RuntimeError("Marooned! No matching LOOP_END.")

def run(file_path: str):
    instrs, functions = parse(file_path)
    booty = 0
    barrel = []
    ledger = {}
    pc = 0
    call_stack = []

    while pc < len(instrs):
        cmd, arg = instrs[pc]

        if cmd == 'ADD':
            booty += arg
        elif cmd == 'SUB':
            booty -= arg
        elif cmd == 'MULTIPLY':
            booty *= arg
        elif cmd == 'DIVIDE':
            if arg == 0:
                raise RuntimeError("Ye can't divide by zero, matey!")
            booty = booty // arg
        elif cmd == 'PUSH':
            barrel.append(booty)
        elif cmd == 'FETCH':
            print(booty)
        elif cmd == 'PRINT':
            print(arg)
        elif cmd == 'POP':
            if not barrel:
                raise RuntimeError("The barrel be empty!")
            booty = barrel.pop()
        elif cmd == 'STORE':
            ledger[arg] = booty
        elif cmd == 'LOAD':
            if arg not in ledger:
                raise RuntimeError(f"There be no booty named '{arg}' in the ledger!")
            booty = ledger[arg]
        elif cmd == 'SWAB':
            booty = 0
        elif cmd == 'CALL':
            if arg not in functions:
                raise RuntimeError(f"Avast! No such function '{arg}'")
            call_stack.append(pc)
            sub_instrs, _ = parse_lines(functions[arg])
            run_function(sub_instrs, ledger, barrel)
            pc = call_stack.pop()
        elif cmd == 'INPUT':
            booty = int(input("Parrot squawks: Enter yer booty! "))
        elif cmd == 'LOOP_START':
            if booty != 0:
                call_stack.append(pc)
            else:
                pc = find_matching_end(pc, instrs)
        elif cmd == 'LOOP_END':
            if booty != 0:
                pc = call_stack[-1]
            else:
                call_stack.pop()
        elif cmd == 'EXIT':
            break
        elif cmd == 'RUM':
            booty = random.randint(1, 100)
        else:
            raise RuntimeError(f"Avast! Unknown cmd: {cmd}")

        pc += 1

def parse_lines(lines):
    from parser import COMMAND_PATTERNS
    parsed = []
    for line in lines:
        matched = False
        for pattern, action in COMMAND_PATTERNS:
            m = pattern.match(line)
            if m:
                parsed.append(action(m))
                matched = True
                break
        if not matched:
            raise ParseError(f"Blimey! Couldn't understand: {line}")
    return parsed, {}

def run_function(instructions, ledger, barrel):
    booty = 0
    pc = 0
    call_stack = []

    while pc < len(instructions):
        cmd, arg = instructions[pc]

        if cmd == 'ADD':
            booty += arg
        elif cmd == 'SUB':
            booty -= arg
        elif cmd == 'MULTIPLY':
            booty *= arg
        elif cmd == 'DIVIDE':
            if arg == 0:
                raise RuntimeError("Ye can't divide by zero!")
            booty = booty // arg
        elif cmd == 'PUSH':
            barrel.append(booty)
        elif cmd == 'FETCH':
            print(booty)
        elif cmd == 'PRINT':
            print(arg)
        elif cmd == 'POP':
            if not barrel:
                raise RuntimeError("Empty barrel in function!")
            booty = barrel.pop()
        elif cmd == 'STORE':
            ledger[arg] = booty
        elif cmd == 'LOAD':
            if arg not in ledger:
                raise RuntimeError(f"Ledger be empty for '{arg}'!")
            booty = ledger[arg]
        elif cmd == 'SWAB':
            booty = 0
        elif cmd == 'INPUT':
            booty = int(input("Parrot squawks (in function): "))
        elif cmd == 'EXIT':
            break
        elif cmd == 'RUM':
            booty = random.randint(1, 100)
        pc += 1

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <file.ahoy>")
    else:
        run(sys.argv[1])