import re
def parse_record(line: s) -> dict:
    ls = list(line.split(";"))
    if len(ls) != 3:
        raise ValueError()
    res = {}
    res["city"] = ls[0]
    res["temperature"] = int(ls[1])
    res["date"] = ls[2]
    pattern = re.compile("^%d+-(1[0-2]|0%d)-([0-2]%d|3[0-1])$")
    if not(pattern.match(ls[2])):
        raise ValueError()
    return res

def read_valid(lines: list[str]) -> list[dict]:
    res = []
    for i in lines:
        try:
            stdict = parse_record(i)
            res.append(stdict)
        except:
            continue

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for i in records:
        total[i["city"]] = total.get(i["city"], 0) + float(i["temperature"])
        count[i["city"]] = count.get(i["city"], 0) + 1
    res = {}
    for city in total:
        res[city] = total[city] / count[city]
    sorted_res = sorted(res.items(), key = lambda x : x[0])
    result = dict(sorted_res)
    return result

def warmest_city(records: list[dict]) -> str:
    average = average_by_city(records)
    res = ""
    mx = -10 ** 5
    for i in average:
        if average[i] > mx:
            mx = average[i]
            res = i
    return res
    
