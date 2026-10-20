def count_by_extension(paths):
    res = {}
    for i in paths:
        i_sp = i.strip().split(".")
        res[i_sp[-1]] = res.get(i_sp[-1], 0) + 1
    return res
