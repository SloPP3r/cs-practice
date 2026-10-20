from logstats import *

path = input()
lines = []
with open(path, encoding="utf-8") as log:
    for line in log:
        lines.append(line)
cnt = count_levels(lines)
print(sum(cnt[x] for x in cnt))
print(cnt["ERROR"])
print(cnt["BROKEN"])
