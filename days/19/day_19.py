from collections import defaultdict
import re

def parse_rules(lines, verbose=False):
    rules = defaultdict(list)
    # to_complete = set()
    influences = defaultdict(set)
    complete_rules = []

    # First pass to analyze the dependencies
    for l in lines:
        if len(l) == 0:
            break
        [rule_idx, rule_descr] = l.split(": ")
        rule_idx = int(rule_idx)
        for rule_option in rule_descr.split(" | "):
            # if verbose:
            #     print("Rule {}: {}".format(rule_idx, rule_option))
            if '"' in rule_option:
                rules[rule_idx] = rule_option.replace('"', '')
                complete_rules.append(rule_idx)
            else:
                depends_on = [int(n) for n in rule_option.split(' ')]
                rules[rule_idx].append(depends_on)
                # to_complete.add(rule_idx)
                for dependency in depends_on:
                    influences[dependency].add(rule_idx)
        if verbose:
            print("Rule {} = {}".format(rule_idx, rules[rule_idx]))
    
    # Now we use the complete rules to fill the other
    while len(complete_rules) > 0:
        complete_r = complete_rules.pop(0)
        rule_val = rules[complete_r]
        for incomplete_r in influences[complete_r]:
            new_rule = []
            for rule_opt in rules[incomplete_r]:
                new_rule.append([rule_val if elt==complete_r else elt for elt in rule_opt])
            is_complete = all(all(type(elt) == str for elt in opt) for opt in new_rule)
            if is_complete:
                complete_rules.append(incomplete_r)
                new_rule = '(' + '|'.join(''.join(s for s in opt) for opt in new_rule) + ')'
            rules[incomplete_r] = new_rule
                

    if verbose:
        print("Rules parsed:")
        for i, r in rules.items():
            print("{}: {}".format(i, r))
    return rules

def part_one(lines, verbose=False):
    rules = parse_rules(lines, verbose=verbose)
    pattern = "^" + rules[0] + "$"
    if verbose:
        print("Pattern: {}".format(pattern))
    s = 0
    for l in lines:
        if not(l.isalpha()):
            continue
        if re.match(pattern, l):
            if verbose:
                print("Match line {}".format(l))
            s += 1
        elif verbose:
            print("No match for line {}".format(l))
    return s


def parse_input(path, verbose=False):
    with open(path) as f:
        data = [l.rstrip() for l in f.readlines()] 
    return data


if __name__ == "__main__":
    input_ex = parse_input("input_example.txt", verbose=True)
    assert(part_one(input_ex, verbose=True) == 2), "Wrong output for part one"
    # assert(part_two(input_ex, verbose=True) == sum([elt[1] for elt in examples.values()])), "Wrong output for part two"

    input_puzzle = parse_input("input.txt")
    print("Part one:", part_one(input_puzzle, verbose=False))
    # print("Part two:", part_two(input_puzzle, verbose=False))


