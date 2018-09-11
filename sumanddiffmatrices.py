
def sumanddiff(cdtm1):
    pxpy = np.zeros((160), dtype=int)
    for i in range(0, 81):
        for j in range(0, 81):
            pxpy[i + j] = pxpy[i + j] + cdtm1[i][j]
