from sys import argv
from re import sub
from itertools import combinations


def get_data_from_file(file_name):
    with open(file_name) as f:
        line = f.readline()
        while line:
            max_weight, packs = line.split(':')
            yield (
                float(max_weight),
                tuple(sub('[()$]', '', p).split(',') for p in packs.split())
            )
            line = f.readline()


def run(data):
    for max_possible_weight, packs in data:
        max_sum = 0
        max_weight = 0
        res = '-'
        for combs in sum((list(combinations(packs, l)) for l in range(1, len(packs) + 1)), []):
            current_sum = 0
            current_weight = 0
            current_ids = []
            for p in combs:
                current_ids.append(p[0])
                current_weight += float(p[1])
                current_sum += int(p[2])
            if (
                current_weight <= max_possible_weight
                and (
                    current_sum > max_sum
                    or
                    (current_sum == max_sum and current_weight < max_weight)
                )
            ):
                max_sum, max_weight, res = current_sum, current_weight, current_ids
        print ','.join(res)


run(get_data_from_file(argv[1]))
