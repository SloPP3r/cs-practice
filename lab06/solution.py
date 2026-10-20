def count_by_extension(paths):
    res = {}
    for i in paths:
        i_sp = i.strip().split(".")
        if "." in i:
            res[i_sp[-1].lower()] = res.get(i_sp[-1].lower(), 0) + 1
        else:
            res[""] = res.get("", 0) + 1
    return res

def deepest_path(paths):
    mx = 0
    res = ""
    for i in paths:
        i_sp = i.strip().split("/")
        ln_ph = len(i_sp)
        if ln_ph > mx:
            res = i
            mx = ln_ph
    return res

def human_size(n_bytes):
    alph = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ"]
    cnt = 0
    while n_bytes // 1024 >= 1:
        n_bytes /= 1024
        cnt += 1
    res = str(n_bytes)+ " " + alph[cnt]
    return res
