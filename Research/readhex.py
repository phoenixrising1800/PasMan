# https://www.geoffreybrown.com/blog/a-hexdump-program-in-python/

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("FILE", help="the name of the file to dump", type=str)
args = parser.parse_args()

try:
    with open(args.FILE, "rb") as f:
        n = 0           # block number
        b = f.read(16)  #bytes

        while b:
            print(f"{n * 16:08x} {b}") #fmt. addr. as 8 hex dig. w/ leading 0s
            
            n += 1
            b = f.read(16)

except Exception as e:
    print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)
