from logstats import *

path = input()
lines = []
with open(path, encoding="utf-8") as log:
    for line in log:
        lines.append(line)
cnt = count_levels(lines)
print(sum(cnt[x] for x in cnt))
print(cnt.get("ERROR", 0))
print(cnt.get("BROKEN", 0))

rep = format_report(cnt, top_errors(lines, 3))
with open("report.txt", "w", encoding="utf-8") as file:
    file.write(rep)
