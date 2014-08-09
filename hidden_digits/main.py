import sys


def get_hidden_digits(file_name):
    lines = None
    with open(file_name, 'rb') as f:
        lines = tuple(f.readlines())

    for line in lines:
        res_line = []
        for c in line:
            o = ord(c)
            if o >= 48 and o <= 57:
                res_line.append(c)
            elif o >= 97 and o <= 106:
                res_line.append(str(o - 97))
        print ''.join(res_line) or 'NONE'

get_hidden_digits(sys.argv[1])
