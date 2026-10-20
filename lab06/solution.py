def count_by_extension(paths):
    res = {}
    for i in paths:
        i_sp = i.strip().split(".")
        if "." in i:
            res[i_sp[-1]] = res.get(i_sp[-1], 0) + 1
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
