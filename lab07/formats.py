def csv_to_records(text):
    lines = text.split("\n")
    title = lines[0].split(",")
    ttl_lst = []
    for i in title:
        ttl_lst.append(i.strip())
    res = []
    columns = len(ttl_lst)
    for i in range(1, len(lines)):
        if lines[i].strip() == "":
            continue
        ln = {}
        line_split = lines[i].split(",")
        for j in range(columns):
            ln[ttl_lst[j]] = line_split[j].strip()
        res.append(ln)
    return res

