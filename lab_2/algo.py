def bose_nelson(data):
    m = 1
    while m < len(data):
        j = 0
        while j + m < len(data):
            bose_nelson_merge(j, m, m, data)
            j = j + m + m
        m = m + m
    return data

def bose_nelson_merge(j, r, m, data):
    if j + r < len(data):
        if m == 1:
            if data[j] > data[j + r]:
                data[j], data[j + r] = data[j + r], data[j]
        else:
            m = m // 2
            bose_nelson_merge(j, r, m, data)
            if j + r + m < len(data):
                bose_nelson_merge(j + m, r, m,data)
            bose_nelson_merge(j + m, r - m, m,data)
    return data
