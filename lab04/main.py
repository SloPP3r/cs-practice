import sys
from stats import *
lines = sys.stdin.read().splitlines()
cnt = 0
check_lines = read_valid(lines)
print(len(check_lines))
print(cnt)
avg = average_by_city(check_lines)
best = avg[warmest_city(check_lines)]
print("%.1f" % best)
