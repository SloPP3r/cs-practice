def parse_event(line: str) -> dict:
    res = {}
    sample = ["DEBUG", "INFO", "WARNING", "ERROR"]
    spl = line.split(" ")
    res["time"] = spl[0]
    if spl[1] not in sample:
        raise ValueError()
    res["level"] = spl[1]
    res["message"] = "".join(spl[2:])
    return res

def count_levels(lines: list[str]) -> dict:
    res = {"BROKEN" : 0, "DEBUG" : 0, "ERROR" : 0, "INFO" : 0, "WARNING" : 0}
    for i in lines:
        if i == "" or i == "\n":
            continue
        try:
            line = parse_event(i)
            res[line["event"]] = res.get[line["event"]] + 1
        except:
            res["BROKEN"] = res["BROKEN"] + 1
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
    res = list(msgs.items())
    res = sorted(res, key = lambda x : x[1], reverse = True)
    res = res[:n]
    print(res)
    return res

def format_report(counts: dict, errors: list[list]) -> str:
    res = "Отчёт по журналу\n\n\n"
    for i in counts:
        res += f"{i}: {counts[i]}\n"
    res += "\n\nЧастые ошибки:"
    for i in errors:
        res += f"\n- {i[0]} - {i[1]}"
    return res
