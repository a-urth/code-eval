import sys


def roll_coast(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = f.readlines()

    for line in lines:
        upper = True
        for c in line:
            if c.isalpha():
                if upper:
                    sys.stdout.write(c.upper())
                    upper = False
                else:
                    sys.stdout.write(c.lower())
                    upper = True
            else:
                sys.stdout.write(c)
        sys.stdout.flush()

roll_coast(sys.argv[1])
