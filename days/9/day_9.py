def check_valid_number(preamble, n):
    possible_sums = set(preamble[i] + preamble[j] for i in range(len(preamble)) for j in range(i+1, len(preamble)))
    return n in possible_sums

def part_one(lines, verbose=False, preamble_size=25):
    for i in range(preamble_size, len(lines)):
        if not check_valid_number(lines[i-preamble_size:i], lines[i]):
            if verbose:
                print("Element #{} (={}) is not valid!".format(i, lines[i]))
            return lines[i]
        if verbose:
            print("#{} (={}) is valid".format(i, lines[i]))
    

def part_two(lines, goal, verbose=False):
    i = 0
    while lines[i] < goal:
        if verbose:
            print("i={}".format(i))
        j = i+1
        while i+j<len(lines) and sum(lines[i:j]) < goal:
            j += 1
        if verbose:
            print("Stopping at j={}".format(j))
        if sum(lines[i:j]) == goal:
            if verbose:
                print("Goal reached: {}".format(lines[i:j]))
            return min(lines[i:j]) + max(lines[i:j])
        else:
            i += 1

if __name__ == "__main__":
    with open("input_example_day_9.txt") as f_in_ex:
        input_example = [int(s) for s in f_in_ex.readlines()]
    
    print(input_example)
    assert(part_one(input_example, verbose=False, preamble_size=5) == 127), "Wrong output for part one"
    assert(part_two(input_example, goal=127, verbose=False) == 62), "Wrong output for part two"

    with open("input_day_9.txt") as f_input:
        puzzle_input = [int(s) for s in f_input.readlines()]
    
    
    result_part_one = part_one(puzzle_input, verbose=False)
    print("Part one:", result_part_one)
    print("Part two:", part_two(puzzle_input, goal=result_part_one, verbose=False))