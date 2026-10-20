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
