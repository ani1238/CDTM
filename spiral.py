import numpy as np


def compp(tocomp, mid):
    if tocomp > mid:
        return 2
    if tocomp == mid:
        return 1
    return 0


def spiral(n, mat):
    '''
    n = 3
    mat = np.array([[1, 3, 5, 7, 3, 4],
                    [6, 2, 8, 9, 7, 6],
                    [5, 7, 8, 7, 2, 1],
                    [0, 0, 1, 3, 5, 9],
                    [2, 2, 5, 4, 1, 6],
                    [2, 1, 8, 9, 3, 0]])
    '''
    len, wid = mat.shape()
    cdtm = []
    h = (int)(n / 2)
    for i in range(h, wid - h):
        for j in range(h, len - h):
            mid = mat[i][j]
            sti = i - h
            stj = j - h
            eni = i + h
            enj = j + h
            cdtmeach = []
            while sti < eni and stj < enj:
                for a in range(stj, enj + 1):
                    cdtmeach.append(compp(mat[sti][a], mid))
                sti = sti + 1
                for a in range(sti, eni + 1):
                    cdtmeach.append(compp(mat[a][enj], mid))
                enj = enj - 1
                for a in range(enj, stj - 1, -1):
                    cdtmeach.append(compp(mat[eni][a], mid))
                eni = eni - 1
                for a in range(eni, sti - 1, -1):
                    cdtmeach.append(compp(mat[a][stj], mid))
                stj = stj + 1
            cdtm.append(cdtmeach)
            # print(cdtmeach)
    cdtm = np.array(cdtm)

    print(cdtm)


spiral()
