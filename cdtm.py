import numpy as np
import cv2
import os
def Normalise(img):
    Nx,Ny=img.shape[:2]
    R=2*Nx*(Ny-1)+2*Ny*(Nx-1)+4*(Nx-1)*(Ny-1)
    img=np.array(img/R,dtype=float)
    return img

def compp(tocomp, mid):
    if tocomp > mid:
        return 2
    if tocomp == mid:
        return 1
    return 0


def cdtm(n, mat):
    '''
    n = 3
    mat = np.array([[1, 3, 5, 7, 3, 4],
                    [6, 2, 8, 9, 7, 6],
                    [5, 7, 8, 7, 2, 1],
                    [0, 0, 1, 3, 5, 9],
                    [2, 2, 5, 4, 1, 6],
                    [2, 1, 8, 9, 3, 0]])
    '''
    len, wid = mat.shape[:2]
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

    return cdtm



##def od1(img):
##            cdtmarr=cdtm(img)
##            cdtm1=np.zeros([81,81])
##            for j in range(cdtmarr.shape[0]):
##                nctu=0
##                ndtu=0
##                power=0
##                for i in range(1,8,2):
##                    nctu=nctu+cdtmarr[j][i]*pow(3,power)
##                    ndtu=ndtu+cdtmarr[j][i-1]*pow(3,power)
##                    power=power+1
##                cdtm1[nctu][ndtu]=cdtm1[nctu][ndtu]+1
##
##
##            return cdtm1


def od2(img,x,y):
            cdtmarr=cdtm(3,img)
            cdtm1=np.zeros([81,81])
            for j in range(cdtmarr.shape[0]):
                nctu=0
                ndtu=0
                power=0
                ind1=x*2+1
                ind2=y*2
                for i in range(4):
                    nctu=nctu+cdtmarr[j][(ind1)%8]*pow(3,power)
                    ndtu=ndtu+cdtmarr[j][(ind2)%8]*pow(3,power)
                    power=power+1
                    ind1+=2
                    ind2+=2
                cdtm1[nctu][ndtu]=cdtm1[nctu][ndtu]+1
                print(nctu,ndtu)

            return cdtm1



img=np.array([[5,6,7,1,2],[3,4,1,2,9],[1,2,3,4,5],[4,5,7,9,1],[2,3,4,5,2]])
od2(img,0,0)
path=(os.getcwd()+'\data')
imgdir=os.listdir(path)
print(imgdir)
for i in imgdir:
    data=os.listdir(path+'\\'+i)
    for j in data:
        img=cv2.imread((path+'\\'+i+'\\'+j),0)
        img=np.array(img)
##        print(od1(img))
        break
    #print(data)
    break
            



