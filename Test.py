from itertools import (takewhile,repeat)

def rawincount_lf(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum( buf.count(b'\n') for buf in bufgen )

def rawincount_crlf(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum( buf.count(b'\r\n') for buf in bufgen )

print('Total lf:', rawincount_lf("Test.csv"))
print('Total crlf', rawincount_crlf("Test.csv"))
