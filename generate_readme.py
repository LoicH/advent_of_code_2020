import os
import re

pattern_url_exercise = "https://adventofcode.com/2020/day/{}"
pattern_url_solution = "https://github.com/LoicH/advent_of_code_2020/blob/master/days/{}/day_{}.py"

pattern_file_solution = r"day_(\d+).py"
if os.path.exists("README.md"):
    os.remove("README.md")

for f in sorted(os.listdir("days")):
    if not os.path.isdir(os.path.join("days", f)):
        continue
    n = f
    s = "- Day {}: [Exercise]({}) | [Solution]({})\n".format(n, pattern_url_exercise, pattern_url_solution)
    with open("README.md", 'a') as f_out:
        f_out.write(s.format(n, n, n))