import itertools


def find_subsets(s, m):
    return set(itertools.combinations(s, m))


if __name__ == '__main__':
    s = {1, 2, 3, 4}
    for m in range(1, len(s)):
        print(find_subsets(s, m))
