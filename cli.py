import argparse
from interpreter import run
from parser import parse
from utils import ParseError

def main():
    parser = argparse.ArgumentParser(prog='ahoy', description='Ahoy! esolang runner')
    parser.add_argument('script', help='Path to .ahoy script')
    parser.add_argument('--mode', choices=['pirate','map'], help='Force parse mode')
    parser.add_argument('--debug', action='store_true', help='Show debug info')
    args = parser.parse_args()

    try:
        if args.debug:
            instrs, funcs = parse(args.script)
            print('== Instructions ==')
            for ins in instrs:
                print(ins)
            print('== Functions ==')
            for fname, lines in funcs.items():
                print(f"{fname}():")
                for line in lines:
                    print(f"  {line}")
            print('== Running ==')
        run(args.script)
    except ParseError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Runtime error: {e}")

if __name__ == '__main__':
    main()