# -*- coding: GBK -*-  
import os
import shutil
import time
import datetime

shLineList=[]
shDateStrList=[]
shPriceOpeningFList=[]
shPriceCloseingFList=[]
shPriceHighestFList=[]
shPriceLowestFList=[]
shTradeVolumeFList=[]

lineList=[]
dateStrList=[]
priceOpeningFList=[]
priceCloseingFList=[]
priceHighestFList=[]
priceLowestFList=[]
tradeVolumeFList=[]
amplitudeFlist=[]  ##���

##���㰴���ڼ�����ͣ����


def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

def calNatureDays(dateStr1,dateStr2):
    d1= convertDateStr2Date(dateStr1)
    d2= convertDateStr2Date(dateStr2)
    return (d1-d2).days

def getDateOfPrice(price,priceFList,dateStrList):
    indexPrice=priceFList.index(price)
    return dateStrList[indexPrice]
    


def highAndlowPriceSH(days):
    print("��������(������/��):\t"+str(days)+"\t��ʼ����:"+shDateStrList[-days]+"\t��������:"+shDateStrList[-1])
    priceHighest=max(shPriceHighestFList[-days:-1])
    print("��������ߵ�:\t"+str(priceHighest))
    datePriceHighest=getDateOfPrice(priceHighest,shPriceHighestFList,shDateStrList)
    print("��������߼�:\t"+str(priceHighest)+"\t��������:\t"+datePriceHighest)
   
    priceLowest=min(shPriceLowestFList[-days:-1])
    datePriceLowest=getDateOfPrice(priceLowest,shPriceLowestFList,shDateStrList)
    print("��������ͼ�:\t"+str(priceLowest)+"\t��������:\t"+datePriceLowest)

   
    
    print("��ߵ��������͵���ֽ����ո���\t"+str(shPriceHighestFList.index(priceHighest)-shPriceLowestFList.index(priceLowest)))
    print("��ߵ�/��͵�:\t"+str(round(priceHighest/priceLowest,2)))


def readStockSH999999():
    print("\n"+"#"*80)
    print ("��ǰ��Ʊ����:"+"sh999999")
    stockDataFile=os.path.join(dataPath,'999999.txt')
    fileOpened=open(stockDataFile,'r')
    lineIndex=0
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        splitLine=line.split()
        if line!="" and lineIndex>=5 and len(splitLine)>=6:
            shLineList.append(line)
            shDateStrList.append(splitLine[0])
            shPriceOpeningFList.append(float(splitLine[1]))
            shPriceHighestFList.append(float(splitLine[2]))
            shPriceLowestFList.append(float(splitLine[3]))
            shPriceCloseingFList.append(float(splitLine[4]))
            shTradeVolumeFList.append(float(splitLine[5]))
    fileOpened.close()
    print("��֤���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+shDateStrList[0]+"��������գ�\t"+shDateStrList[-1])

def readStockByID(stockID):
    print("\n"+"#"*80)
    print("��ǰ��Ʊ����:"+stockID)
    stockDataFile=os.path.join(dataPath,stockID+'.txt')
    fileOpened=open(stockDataFile,'r')
    lineIndex=0
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        splitLine=line.split()
        if line!="" and lineIndex>=5 and len(splitLine)>=6:
            lineList.append(line)
            dateStrList.append(splitLine[0])
            priceOpeningFList.append(float(splitLine[1]))
            priceHighestFList.append(float(splitLine[2]))
            priceLowestFList.append(float(splitLine[3]))
            priceCloseingFList.append(float(splitLine[4]))
            tradeVolumeFList.append(float(splitLine[5]))
    fileOpened.close()
    print(stockID+"���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+dateStrList[0]+"��������գ�\t"+dateStrList[-1])


def analysisDate(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("��������(������/��):\t"+str(indexEnd-indexStart)+"\t��ʼ����:"+dateStrList[indexStart]+"\t��������:"+dateStrList[indexEnd])
    
    priceHighest=max(priceHighestFList[indexStart:indexEnd])
    datePriceHighest=getDateOfPrice(priceHighest,priceHighestFList,dateStrList)
    print("��������߼�:\t"+str(priceHighest)+"\t��������:\t"+datePriceHighest)
    
    priceLowest=min(priceLowestFList[indexStart:indexEnd])
    datePriceLowest=getDateOfPrice(priceLowest,priceLowestFList,dateStrList)
    print("��������ͼ�:\t"+str(priceLowest)+"\t��������:\t"+datePriceLowest)

    natureDaysNumFromLastPeak2Today=-1  
    if datePriceHighest>=datePriceLowest:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceHighest)
    else:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceLowest)
    print("�ϸ���ֵ����������Ȼ�ո���(��):\t"+str(natureDaysNumFromLastPeak2Today.days))
    print("��ߵ��������͵���ֽ����ո���(��):\t"+str(1+priceHighestFList.index(priceHighest)-priceLowestFList.index(priceLowest)))
    daySpan=calNatureDays(datePriceHighest,datePriceLowest)
    print("��ߵ��������͵������Ȼ�ո���(��):\t"+str(daySpan))
    print("��ߵ�/��͵�:\t"+str(round(priceHighest/priceLowest,2)))

def analysisScale(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("�����۲���Ƿ�")
    
    zhenfuFList=[] ## ��������
    zhangdiefuFList=[]  ##�ǵ���
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i]-priceOpeningFList[i])/priceCloseingFList[i-1]
        priceDelta2=(priceHighestFList[i]-priceLowestFList[i])/priceCloseingFList[i-1]
        if priceDelta1>=0.05:
            zhenfuFList.append(i)
        if abs(priceDelta2)>=0.05:
            zhangdiefuFList.append(i)
    strDate=""
    for item in zhenfuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("�������5%����:\t"+str(len(zhenfuFList))+"\t��ʼ�����ǣ�"+strDate)
    strDate=""
    for item in zhangdiefuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("�ǵ�������5%:\t"+str(len(zhangdiefuFList))+"\t��ʼ�����ǣ�"+strDate)



###���������շ���###
def analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("����"+str(numConsecutiveTradeDays)+"�������շ��ȳ���"+str(fScale))
    
    waveFList=[] ## ��������
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i-numConsecutiveTradeDays]-priceCloseingFList[i])/priceCloseingFList[i-numConsecutiveTradeDays]
        if abs(priceDelta1)>=fScale:
            waveFList.append(i)
    strDate=""
    for item in waveFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("���������������:\t"+str(len(waveFList))+"\t��ʼ�����ǣ�"+strDate)

    

def highAndlowPrice(stockID,daysList):
    for days in daysList:
        print("-"*50)
        print("��������(������/��):\t"+str(days)+"\t��ʼ����:"+dateStrList[-days]+"\t��������:"+dateStrList[-1])
        
        priceHighest=max(priceHighestFList[-days:-1])
        datePriceHighest=getDateOfPrice(priceHighest,priceHighestFList,dateStrList)
        print("��������߼�:\t"+str(priceHighest)+"\t��������:\t"+datePriceHighest)
        
        priceLowest=min(priceLowestFList[-days:-1])
        datePriceLowest=getDateOfPrice(priceLowest,priceLowestFList,dateStrList)
        print("��������ͼ�:\t"+str(priceLowest)+"\t��������:\t"+datePriceLowest)

        natureDaysNumFromLastPeak2Today=-1  
        if datePriceHighest>=datePriceLowest:
            natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceHighest)
        else:
            natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceLowest)
        print("�ϸ���ֵ����������Ȼ�ո���(��):\t"+str(natureDaysNumFromLastPeak2Today.days))
        print("��ߵ��������͵���ֽ����ո���(��):\t"+str(1+priceHighestFList.index(priceHighest)-priceLowestFList.index(priceLowest)))
        daySpan=calNatureDays(datePriceHighest,datePriceLowest)
        print("��ߵ��������͵������Ȼ�ո���(��):\t"+str(daySpan))
        print("��ߵ�/��͵�:\t"+str(round(priceHighest/priceLowest,2)))

if __name__=="__main__":
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    startClock=time.clock()
    
    goalFilePath='result.txt'
    dataPath=u"dataStock"

    iDaysPeriodUser=300
    readStockSH999999()
    highAndlowPriceSH(iDaysPeriodUser) 
 

    stockID="600196"
    readStockByID(stockID)
  ##  highAndlowPrice(stockID,[iDaysPeriodUser,30,60,120])
    for item in [iDaysPeriodUser,30,60,120]:
        dateStrStart=dateStrList[-item]
        dateStrEnd=dateStrList[-1]
        analysisDate(stockID,dateStrStart,dateStrEnd)
        analysisScale(stockID,dateStrStart,dateStrEnd)
        numConsecutiveTradeDays=5
        fScale=0.1
        analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale)

    fileWrited=open(goalFilePath,'w')
    fileWrited.write('\n')
    fileWrited.close()

    timeSpan=time.clock()-startClock
    print("Time used(s):",timeSpan)




