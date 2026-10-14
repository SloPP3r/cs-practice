import sys
from stats import *
lines = []
for i in sys.stdin:
    if i == "q\n":
        break
    lines.append(i)
check_lines = read_valid(lines)
print(len(check_lines))
print(cnt)
avg = average_by_city(check_lines)
best = avg[warmest_city(check_lines)]
print("%.1f" % best)
