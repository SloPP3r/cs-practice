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
        i = i[:i.find("#")]
        i = i.strip()
        if i == "": continue
        if i[-1] == ":":
            name = i
            res[name] = []
            lst = []
        elif i[-1] == "-":
            lst.append(i)
            res[name] = lst
        else:
            i.split(":")
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
            if i[1] == "true":
                val = True
            elif i[1] == "false":
                val = False
            else:
                val = i[1]
            res[i[0]] = val
    return res

                
