import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        lst = x.split()
        new_lst = []
        for i in lst:
            new_lst.append(hex(ord(i)))
        encoded = new_lst.join()
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        lst = x.split('0x')
        new_lst = []
        for i in lst:
            new_lst.append(chr(int(i)))
        decoding = new_lst.join()
        print(decoding)
