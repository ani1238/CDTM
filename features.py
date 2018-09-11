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
            IDM=IDM+(1/(1+(i-j)**2)))*cdtm1[i][j]
    return IDM














