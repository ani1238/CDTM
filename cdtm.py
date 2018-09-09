import numpy as np
import cv2
import os
def cdtm(img):
    height, width = img.shape[:2]
    cdtmarr=[]
    for i in range(height-2):
        for j in range(width-2):
            if(img[i][j]>img[i+1][j+1]):
                a=2
            if(img[i][j]==img[i+1][j+1]):
                a=1
            if(img[i][j]<img[i+1][j+1]):
                a=0
            if(img[i][j+1]>img[i+1][j+1]):
                b=2
            if(img[i][j+1]==img[i+1][j+1]):
                b=1
            if(img[i][j+1]<img[i+1][j+1]):
                b=0
            if(img[i][j+2]>img[i+1][j+1]):
                c=2
            if(img[i][j+2]==img[i+1][j+1]):
                c=1
            if(img[i][j+2]<img[i+1][j+1]):
                c=0
            if(img[i+1][j+2]>img[i+1][j+1]):
                d=2
            if(img[i+1][j+2]==img[i+1][j+1]):
                d=1
            if(img[i+1][j+2]<img[i+1][j+1]):
                d=0
            if(img[i+2][j+2]>img[i+1][j+1]):
                e=2
            if(img[i+2][j+2]==img[i+1][j+1]):
                e=1
            if(img[i+2][j+2]<img[i+1][j+1]):
                e=0
            if(img[i+2][j+1]>img[i+1][j+1]):
                f=2
            if(img[i+2][j+1]==img[i+1][j+1]):
                f=1
            if(img[i+2][j+1]<img[i+1][j+1]):
                f=0
            if(img[i+2][j]>img[i+1][j+1]):
                g=2
            if(img[i+2][j]==img[i+1][j+1]):
                g=1
            if(img[i+2][j]<img[i+1][j+1]):
                g=0
            if(img[i+1][j]>img[i+1][j+1]):
                h=2
            if(img[i+1][j]==img[i+1][j+1]):
                h=1
            if(img[i+1][j]<img[i+1][j+1]):
                h=0
            cdtmarr.append([a,b,c,d,e,f,g,h])
    cdtmarr=np.array(cdtmarr)
    print(cdtmarr)
    return cdtmarr
    


def od1(img):
            cdtmarr=cdtm(img)
            cdtm1=np.zeros([81,81])
            for j in range(cdtmarr.shape[0]):
                nctu=0
                ndtu=0
                power=0
                for i in range(1,8,2):
                    nctu=nctu+cdtmarr[j][i]*pow(3,power)
                    ndtu=ndtu+cdtmarr[j][i-1]*pow(3,power)
                    power=power+1
                cdtm1[nctu][ndtu]=cdtm1[nctu][ndtu]+1


            return cdtm1




img=np.array([[5,6,7,1,2],[3,4,1,2,9],[1,2,3,4,5],[4,5,7,9,1],[2,3,4,5,2]])
print(od1(img))
print(os.listdir())
            



