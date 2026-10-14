import sys
from stats import *
lines = sys.stdin.read().splitlines()
check_lines = read_valid(lines)
print(len(check_lines))
print(len(lines) - len(check_lines))
best = warmest_city(check_lines)
print("%.1f" % best)
