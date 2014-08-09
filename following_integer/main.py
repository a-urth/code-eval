import sys
from itertools import permutations


def find_next_int(file_name):
    with open(file_name, 'r') as f:
        for num in f:
            num = num.strip()
            l = sorted(set(int(''.join(r)) for r in permutations(num + '0')))
            print l[l.index(int(num)) + 1]


find_next_int(sys.argv[1])
