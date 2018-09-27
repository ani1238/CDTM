import numpy as np
def CDTMnormalise(cdtm1):
    Sum=np.sum(cdtm1)
    cdtm1=np.array(cdtm1/Sum)
    return cdtm1

def rowSum(cdtm1):
    rowSum=np.sum(cdtm1,axis=1)
    return rowSum

def columnSum(cdtm1):
    columnSum=np.sum(cdtm1,axis=0)
    return columnSum

def meanX(cdtm1):
    rowSum=rowSum(cdtm1)
    meanX=0
    for i in range(0,81):
        meanX=meanX+i*rowSum[i]
    return meanX


def meanY(cdtm1):
    columnSum=columnSum(cdtm1)
    meanY=0
    for i in range(0,81):
        meanY=meanY+i*columnSum[i]
    return meanY

def STdevX(cdtm1):
    rowSum=rowSum(cdtm1)
    meanX=meanX(cdtm1)
    stdX=0
    for i in range(81):
        stdX=stdX+((i-meanX)**2)*rowSum
    return sqrt(stdX)

def STdevY(cdtm1):
    columnSum=columnSum(cdtm1)
    meanY=meanY(cdtm1)
    stdY=0
    for i in range(81):
        stdY=stdY+((i-meanY)**2)*columnSum
    return sqrt(stdY)

def correlation(cdtm1):
    meanX=meanX(cdtm1)
    meanY=meanY(cdtm1)
    stdX=STdevX(cdtm1)
    stdY=STdevY(cdtm1)

    correlation=0
    for i in range(81):
        for j in range(81):
            correlation=correlation+((i*j)*cdtm1[i][j]-meanX*meanY)/(stdX*stdY)
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
    (rows,columns)=np.shape(cdtm1)
    for i in range (rows):
        result=result+((i-meanX)**2)*rowSum[i]

def summatrix(cdtm1):
    pxpy = np.zeros((160), dtype=int)
    for i in range(0, 81):
        for j in range(0, 81):
            pxpy[i + j] = pxpy[i + j] + cdtm1[i][j]
    return pxpy


def diffmatrix(cdtm1):
    pxmy = np.zeros((80), dtype=int)
    for i in range(0, 81):
        for j in range(0, 81):
            pxmy[abs(i - j)] = pxmy[abs(i - j)] + cdtm1[i][j]
    return pxmy


def entropy(cdtm1):
    l, w = cdtm1.shape()
    ans = 0
    for i in l:
        for j in w:
            ans = ans + (cdtm1[i][j] * (math.log2(cdtm1[i][j])))
    return ans


def sumentropy(cdtm1):
    pxpy=summatrix(cdtm1)
    ans = 0
    for i in range(0, 161):
        ans = ans + (pxpy[i] * (log2(pxpy[i])))
    return -1 * ans


def differenceentropy(cdtm1):
    pxmy=diffmatrix(cdtm1)
    ans = 0
    for i in range(0, 81):
        ans = ans + (pxmy[i] * (log2(pxmy[i])))
    return -1 * ans

def sumAverage(cdtm1):
    pxpy=summatrix(cdtm1)
    ans=0
    for in range(0,161):
        ans=ans+i*pxpy[i]
    return ans

def contrast(cdtm1):
    ans=0
    for i in range(0,81):
        for j in range(0,81):
            ans=ans+(i-j)**2+cdtm1[i][j]
    return ans

def energy(cdtm1):
    ans=0;
    for i in range(0,81):
        for j in range(0,81):
            ans=ans+cdtm1[i][j]**2
    return ans






