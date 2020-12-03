
def part_one(txt, slope, verbose):
    trees_seen = 0
    lines = txt.split('\n')
    width = len(lines[0])
    i, j = 0, 0
    while i<len(lines):
        if lines[i][j] == '#':
            trees_seen += 1
        i += slope[1]
        j = (j+slope[0]) % width
    return trees_seen
    
def part_two(txt, slopes, verbose):
    product = 1
    for s in slopes:
        p = part_one(txt, s, verbose=False)
        product *= p
        if verbose:
            print("After slope {}, saw {} trees, product is now {}".format(s, p, product))
    return product

# checking the input example
with open("input_example_day_3.txt") as f:
    example = f.read()

assert (part_one(example, slope=(3,1), verbose=False) == 7), "Wrong result for part one"

# computing the input example
with open("input_day_3.txt") as f:
    input_day = f.read()
print("Part one:", part_one(input_day, slope=(3,1), verbose=False))

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
assert (part_two(example, slopes, verbose=True) == 336), "Wrong result for part two"

print("Part two:", part_two(input_day, slopes, False))