def parse_event(line: str) -> dict:
    res = {}
    line = line.replace("\n", "")
    for i in range(len(line)):
        line[i] = line[i].strip()
    sample = ["DEBUG", "INFO", "WARNING", "ERROR"]
    spl = line.split(" ")
    res["time"] = spl[0]
    if spl[1] not in sample:
        raise ValueError()
    res["level"] = spl[1]
    res["message"] = " ".join(spl[2:])
    return res

def count_levels(lines: list[str]) -> dict:
    res = {}
    for i in lines:
        i = i.replace("\n", "").strip()
        if i == "" or i == "\n":
            continue
        try:
            line = parse_event(i)
            res[line["level"]] = res.get(line["level"], 0) + 1
        except:
            res["BROKEN"] = res.get("BROKEN", 0) + 1
    return res

def top_errors(lines: list[str], n: int) -> list[list]:
    msgs = {}
    for i in lines:
        if i == "" or i == "\n":
            continue
        try:
            line = parse_event(i)
            if line["level"] == "ERROR":
                msgs[line["message"]] = msgs.get(line["message"], 0) + 1
        except:
            continue
    res = msgs.items()
    res = list(map(list, res))
    res = sorted(res, key = lambda x : x[1], reverse = True)
    res = res[:n]
    return res

def format_report(counts: dict, errors: list[list]) -> str:
    counts = dict(sorted(counts.items(), key = lambda x : x[0]))
    res = "Отчёт по журналу\n\n"
    for i in counts:
        res += f"{i}: {counts[i]}\n"
    res += "\nЧастые ошибки:"
    for i in errors:
        res += f"\n- {i[0]} — {i[1]}"
    res += "\n"
    return res
