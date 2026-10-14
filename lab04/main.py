import sys
lines = []
for line in sys.stdin:
    city, temp, date = line.split(";")
    total[city] = total.get(city, 0) + float(temp)
    count[city] = count.get(city, 0) + 1
best = ""
for city in total:
    if best == "" or total[city] / count[city] > total[best] / count[best]:
        best = city
print(len(lines))
print(0)
print(total[best] / count[best])
