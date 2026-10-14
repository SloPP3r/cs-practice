import sys
from stats import *
lines = sys.stdin.read().splitlines()
check_lines = read_valid(lines)
print(len(check_lines))
print(len(lines)-len(check_lines) - lines.count("") - lines.count("\n"))
avg = average_by_city(check_lines)
best = avg[warmest_city(check_lines)]
print("%.1f" % best)
