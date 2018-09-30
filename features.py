import numpy as np
import math
def CDTMnormalise(cdtm1):
    Sum=np.sum(cdtm1)
    cdtm1=np.array(cdtm1/Sum)
    return cdtm1

def rowSum(cdtm1):
    rowsum=np.sum(cdtm1,axis=1)
    return rowsum

def columnSum(cdtm1):
    columnSum=np.sum(cdtm1,axis=0)
    return columnSum

def meanX(cdtm1):
    rowsum=0
    rowsum=rowSum(cdtm1)
    meanx=0
    for i in range(0,81):
        meanx=meanx+i*rowsum[i]
    return meanx


def meanY(cdtm1):
    columnsum=columnSum(cdtm1)
    meanY=0
    for i in range(0,81):
        meanY=meanY+i*columnsum[i]
    return meanY

def STdevX(cdtm1):
    rowsum=rowSum(cdtm1)
    meanx=meanX(cdtm1)
    stdX=0
    for i in range(81):
        stdX=stdX+((i-meanx)**2)*rowsum[i]
    
    return math.sqrt(stdX)

def STdevY(cdtm1):
    columnsum=columnSum(cdtm1)
    meany=meanY(cdtm1)
    stdY=0
    for i in range(81):
        stdY=stdY+((i-meany)**2)*columnsum[i]
    return math.sqrt(stdY)   

def correlation(cdtm1):
    meanx=meanX(cdtm1)
    meany=meanY(cdtm1)
    stdX=STdevX(cdtm1)
    stdY=STdevY(cdtm1)
    correlation=0
    for i in range(81):
        for j in range(81):
            correlation=correlation+((i*j)*cdtm1[i][j]-meanx*meany)/(stdX*stdY)
    return correlation

def IDM(cdtm1):
    IDM=0
    for i in range(81):
        for j in range(81):
            IDM=IDM+(1/(1+(i-j)**2))*cdtm1[i][j]
    return IDM


def angular_second_moment(cdtm1):
    result=0
    (rows,columns)=np.shape(cdtm1)
    for i in range (rows) :
        for j in range (columns):
            result=result+cdtm1[i][j]**2
    return result
def varianceX(cdtm1):
    result=0
    rowsum=rowSum(cdtm1)
    meanx=meanX(cdtm1)
    (rows,columns)=np.shape(cdtm1)
    for i in range (rows):
        result=result+((i-meanx)**2)*rowsum[i]
    return result

def summatrix(cdtm1):
    pxpy = np.zeros((161), dtype=float)
    for i in range(0, 81):
        for j in range(0, 81):
            pxpy[i + j] = pxpy[i + j] + cdtm1[i][j]
    #print(pxpy)
    return pxpy


def diffmatrix(cdtm1):
    pxmy = np.zeros((81), dtype=float)
    for i in range(0, 81):
        for j in range(0, 81):
            pxmy[abs(i - j)] = pxmy[abs(i - j)] + cdtm1[i][j]
    return pxmy


def entropy(cdtm1):
    l, w = cdtm1.shape[:2]
    ans = 0.0
    for i in range(l):
        for j in range(w):
            if(cdtm1[i][j]!=0):
                ans = ans + (cdtm1[i][j] * math.log(cdtm1[i][j],2.0))
            
    return ans


def sumentropy(cdtm1):
    pxpy=summatrix(cdtm1)
    ans = 0.0
    for i in range(0, 161):
        if(pxpy[i]!=0):
            ans = ans + (pxpy[i] *math.log((pxpy[i]),2) )
        
    return -1 * ans


def differenceentropy(cdtm1):
    pxmy=diffmatrix(cdtm1)
    ans = 0.0
    for i in range(0, 81):
        if(pxmy[i]!=0):
            ans = ans + (pxmy[i] * math.log((pxmy[i]),2))
        
    return -1 * ans

def sumAverage(cdtm1):
    pxpy=summatrix(cdtm1)
    ans=0.0
    for i in range(0,161):
        ans=ans+i*pxpy[i]
    return ans

def contrast(cdtm1):
    ans=0.0
    for i in range(0,81):
        for j in range(0,81):
            ans=(float)(ans+(float)((i-j)**2)+cdtm1[i][j])
           # print(ans)
    return ans

def energy(cdtm1):
    ans=0.0;
    for i in range(0,81):
        for j in range(0,81):
            ans=ans+cdtm1[i][j]**2
    return ans






