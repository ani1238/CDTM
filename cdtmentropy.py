
def entropy(cdtm1):
    l, w = cdtm1.shape()
    ans = 0
    for i in l:
        for j in w:
            ans = ans + (cdtm1[i][j] * (math.log2(cdtm1[i][j])))
    return ans
