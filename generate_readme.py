import os
import re

pattern_url_exercise = "https://adventofcode.com/2020/day/{}"
pattern_url_solution = "https://github.com/LoicH/advent_of_code_2020/blob/master/{}"

pattern_file_solution = r"day_(\d+).py"
if os.path.exists("README.md"):
    os.remove("README.md")

for f in sorted(os.listdir()):
    m = re.match(pattern_file_solution, f)
    if m:
        s = """## Day {}
### Exercise
{}
### Solution
{}
""".format(m.group(1), pattern_url_exercise, pattern_url_solution)
        with open("README.md", 'a') as f_out:
            f_out.write(s.format(m.group(1), m.group(0)))