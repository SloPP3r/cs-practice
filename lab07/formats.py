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

def parse_settings(lines):
    res = {}
    name = ""
    flag = False
    lst = []
    for i in lines:
        if i.find("#") != -1:
            i = i[:i.find("#")]
        i = i.strip()
        if i == "": continue
        if i[-1] == ":":
            name = i
            res[name] = []
            lst = []
            continue
        elif i[-1] == "-":
            i = i[1:].strip()
            if "." in i or "," in i:
                temp = i[1].replace(",",".")
                try:
                    val = float(temp)
                    lst.append(val)
                    res[name] = lst
                    continue
                except:
                    pass
            else:
                try:
                    val = int(i)
                    res[i[0]] = val
                    lst.append(val)
                    res[name] = lst
                    continue
                except:
                        pass
            if i == "true" or i == "yes":
                val = True
            elif i == "false" or i == "no":
                val = False
            else:
                val = i[1]
            lst.append(val)
            res[name] = lst
        else:
            i = i.split(":")
            i[0] = i[0].strip()
            i[1] = i[1].strip()
            if "." in i[1] or "," in i[1]:
                temp = i[1].replace(",",".")
                try:
                    val = float(temp)
                    res[i[0]] = val
                    continue
                except:
                    pass
            else:
                try:
                    val = int(i[1])
                    res[i[0]] = val
                    continue
                except:
                        pass
            if i[1] == "true" or i[1] == "yes":
                val = True
            elif i[1] == "false" or i[1] == "no":
                val = False
            else:
                val = i[1]
            res[i[0]] = val
    return res

def merge_by_key(rows, extra, key):
    for vl in extra:
        for i in rows:
            if i[key] == vl:
                for j in extra[vl]:
                    if j not in i:
                        i[j] = extra[vl][j]
    return rows

def records_to_json(records):
    res = ""
    res += "[\n  "
    for i in records:
        res += "{\n"
        srt = dict(sorted(i.items(), key = lambda x : x[0]))
        for j in srt:
            res += f'    "{j}": {srt[j]},\n'
        res = res[:-2]
        res += "\n}\n"
    return res
