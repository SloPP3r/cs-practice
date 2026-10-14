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
