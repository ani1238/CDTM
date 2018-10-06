import numpy as np
import cv2
import os
from features import *
import pandas as pd

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
    cdtm1 = []
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
            cdtm1.append(cdtmeach)
    
    cdtm1 = np.asarray(cdtm1)

    return cdtm1


def od2(cdtm1,cdtm2,x,y):
            cdtmarr=cdtm1
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
                cdtm2[nctu][ndtu]=cdtm2[nctu][ndtu]+1
              #  print(nctu,ndtu)

            return cdtm2

cdtm1=np.zeros([81,81])
img=np.array([[5,6,7,1,2],[3,4,1,2,9],[1,2,3,4,5],[4,5,7,9,1],[2,3,4,5,2]])
#cdtm1=od2(cdtm1,img,1,0)
#cdtm1=CDTMnormalise(cdtm1)
#print(cdtm1)
path=(os.getcwd()+'/data')
imgdir=os.listdir(path)
print(imgdir)
for i in imgdir:
        data=os.listdir(path+'/'+i)
        for j in data:
            pos=0
            column=['index']
            for col in range(1,65):
                column.extend(('asm'+str(col),'correlation'+str(col),'variance'+str(col),'idm'+str(col),'entropy'+str(col),'sum_entropy'+str(col),'difference_entropy'+str(col),'sum_avg'+str(col),'contrast'+str(col),'energy'+str(col)))
            df=pd.DataFrame(columns=column)
            #df=pd.DataFrame(columns=['index','asm','correlation','variance','idm','entropy','sum_entropy','difference_entropy','sum_avg','contrast','energy','asm2','correlation2','variance2','idm2','entropy2','sum_entropy2','difference_entropy2','sum_avg2','contrast2','energy2','asm3','correlation3','variance3','idm3','entropy3','sum_entropy3','difference_entropy3','sum_avg3','contrast3','energy3','asm4','correlation4','variance4','idm4','entropy4','sum_entropy4','difference_entropy4','sum_avg4','contrast4','energy4','asm5','correlation5','variance5','idm5','entropy5','sum_entropy5','difference_entropy5','sum_avg5','contrast5','energy5','asm6','correlation6','variance6','idm6','entropy6','sum_entropy6','difference_entropy6','sum_avg6','contrast6','energy6','asm7','correlation7','variance7','idm7','entropy7','sum_entropy7','difference_entropy7','sum_avg7','contrast7','energy7','asm8','correlation8','variance8','idm8','entropy8','sum_entropy8','difference_entropy8','sum_avg8','contrast8','energy8'])
            for ii in os.listdir(path+'/'+i+'/'+j):
                print(ii)
                img=cv2.imread((path+'/'+i+'/'+j+'/'+ii),0)
                img=np.array(img)
                #print(img)
                row=[pos]
                for r in range(0,8):
                    for c in range(0,8):
                        cdtm1=np.zeros((81,81))
                        cdtm2=cdtm(3,img[r*32:(r+1)*32,c*32:(c+1)*32])
                        for k in range (0,4):
                            for l in range(0,4):
                                cdtm1=od2(cdtm2,cdtm1,k,l)
                        cdtm2=CDTMnormalise(cdtm1)
                        row.extend((angular_second_moment(cdtm2),correlation(cdtm2),varianceX(cdtm2),IDM(cdtm2),entropy(cdtm2),sumentropy(cdtm2),differenceentropy(cdtm2),sumAverage(cdtm2),contrast(cdtm2),energy(cdtm2)))
               # print(len(row))
                df.loc[len(df)]=row
                print(len(df))
                pos=pos+1
            df.to_csv(str(j)+'.csv',sep=',')
            #break
        #print(data)
        #break
                



