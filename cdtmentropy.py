
def entropy(cdtm1):
    l, w = cdtm1.shape()
    ans = 0
    for i in l:
        for j in w:
            ans = ans + (cdtm1[i][j] * (math.log2(cdtm1[i][j])))
    return ans


def sumentropy(pxpy):
    ans = 0
    for i in range(0, 161):
        ans = ans + (pxpy[i] * (log2(pxpy[i])))
    return -1 * ans


def differenceentropy(pxmy):
    ans = 0
    for i in range(0, 81):
        ans = ans + (pxmy[i] * (log2(pxmy[i])))
    return -1 * ans
