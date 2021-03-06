## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
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
amplitudeFlist=[]  ##振幅

##计算按周期计算涨停幅度

lineWrited=[]

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
    print("分析周期(交易日/天):\t"+str(days)+"\t起始日期:"+shDateStrList[-days]+"\t结束日期:"+shDateStrList[-1])
    priceHighest=max(shPriceHighestFList[-days:-1])
    print("区间内最高点:\t"+str(priceHighest))
    datePriceHighest=getDateOfPrice(priceHighest,shPriceHighestFList,shDateStrList)
    print("区间内最高价:\t"+str(priceHighest)+"\t出现日期:\t"+datePriceHighest)
   
    priceLowest=min(shPriceLowestFList[-days:-1])
    datePriceLowest=getDateOfPrice(priceLowest,shPriceLowestFList,shDateStrList)
    print("区间内最低价:\t"+str(priceLowest)+"\t出现日期:\t"+datePriceLowest)
   
    print("最高点出现与最低点出现交易日个数\t"+str(shPriceHighestFList.index(priceHighest)-shPriceLowestFList.index(priceLowest)))
    print("最高点/最低点:\t"+str(round(priceHighest/priceLowest,2)))


def readStockSH999999():
    print("\n"+"#"*80)
    print ("当前股票代码:"+"sh999999")
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
    print("上证数据读取完毕,数据开始日：\t"+shDateStrList[0]+"数据结束日：\t"+shDateStrList[-1])

def findPeak(days):
    print('分析周期(天):'+str(days))
    lineWrited.append('-'*50)
    lineWrited.append('分析周期(天):'+str(days))
    lineWrited.append("日期"+"\t局部高点/低点:\t"+"\t距上次峰值交易日个数:\t"+"\t浮动幅度%:\t")
    d1=convertDateStr2Date(shDateStrList[0])
    d2=convertDateStr2Date(shDateStrList[0])
    standValue=100
    days=days/2
    for i in range(days,len(shDateStrList)-days):
##        index, value = max(enumerate(shPriceHighestFList[i-days:i+days]), key=operator.itemgetter(1))
        max_value = max(shPriceHighestFList[i-days:i+days])
        max_index = shPriceHighestFList.index(max_value)
        if max_index==i:
            d2=convertDateStr2Date(shDateStrList[i])
            daysSpan=(d2-d1).days
            lineWrited.append(shDateStrList[i]+"\t"+str(shPriceHighestFList[i])+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            standValue=max_value
           
        min_value = min(shPriceLowestFList[i-days:i+days])
        min_index = shPriceLowestFList.index(min_value)
        if min_index==i:
            d2=convertDateStr2Date(shDateStrList[i])
            daysSpan=(d2-d1).days
            lineWrited.append(shDateStrList[i]+"\t"+str(shPriceLowestFList[i])+"\t"+str(daysSpan)+"\t"+str(round((min_value-standValue)/standValue,3)*100))
            d1=d2
            standValue=min_value
    d2=convertDateStr2Date(shDateStrList[-1])
    daysSpan=(d2-d1).days
    lineWrited.append(shDateStrList[-1]+"\t"+str(shPriceCloseingFList[-1])+"\t"+str(daysSpan)+"\t"+str(round((shPriceCloseingFList[-1]-standValue)/standValue,3)*100))
    

def readStockByID(stockID):
    print("\n"+"#"*80)
    print("当前股票代码:"+stockID)
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
    print(stockID+"数据读取完毕,数据开始日：\t"+dateStrList[0]+"\t数据结束日：\t"+dateStrList[-1])


def analysisDate(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("分析周期(交易日/天):\t"+str(indexEnd-indexStart)+"\t起始日期:"+dateStrList[indexStart]+"\t结束日期:"+dateStrList[indexEnd])
    
    priceHighest=max(priceHighestFList[indexStart:indexEnd])
    datePriceHighest=getDateOfPrice(priceHighest,priceHighestFList,dateStrList)
    print("区间内最高价:\t"+str(priceHighest)+"\t出现日期:\t"+datePriceHighest)
    
    priceLowest=min(priceLowestFList[indexStart:indexEnd])
    datePriceLowest=getDateOfPrice(priceLowest,priceLowestFList,dateStrList)
    print("区间内最低价:\t"+str(priceLowest)+"\t出现日期:\t"+datePriceLowest)

    natureDaysNumFromLastPeak2Today=-1  
    if datePriceHighest>=datePriceLowest:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceHighest)
    else:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceLowest)
    print("上个最值距离今天的自然日个数(天):\t"+str(natureDaysNumFromLastPeak2Today.days))
    print("最高点出现与最低点出现交易日个数(天):\t"+str(1+priceHighestFList.index(priceHighest)-priceLowestFList.index(priceLowest)))
    daySpan=calNatureDays(datePriceHighest,datePriceLowest)
    print("最高点出现与最低点出现自然日个数(天):\t"+str(daySpan))
    print("最高点/最低点:\t"+str(round(priceHighest/priceLowest,2)))

def analysisScale(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("分析价差和涨幅")
    
    zhenfuFList=[] ## 波动幅度
    zhangdiefuFList=[]  ##涨跌幅
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
    print("振幅超过5%天数:\t"+str(len(zhenfuFList))+"\t起始日期是："+strDate)
    strDate=""
    for item in zhangdiefuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("涨跌幅超过5%:\t"+str(len(zhangdiefuFList))+"\t起始日期是："+strDate)


###连续交易日幅度###
def analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("连续"+str(numConsecutiveTradeDays)+"个交易日幅度超过"+str(fScale))
    
    waveFList=[] ## 波动幅度
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i-numConsecutiveTradeDays]-priceCloseingFList[i])/priceCloseingFList[i-numConsecutiveTradeDays]
        if abs(priceDelta1)>=fScale:
            waveFList.append(i)
    strDate=""
    for item in waveFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("振幅超过比例天数:\t"+str(len(waveFList))+"\t起始日期是："+strDate)

##分析股票与大盘走势的同步性
def analysisSynchronization(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("与大盘同步性分析")
    synFile=stockID+"syn.txt"
    fileWrited=open(synFile,'w')
    synFList=[] ## 波动幅度
## 通过日期找到大盘同期index
    fileWrited.write("日期"+"\t"+"大盘涨幅"+"\t"+"股票涨幅"+"\t"+ '同步比例\n')
    for i in range(indexStart,indexEnd):
        dateStrSH=dateStrList[i]
        indexSH=shDateStrList.index(dateStrSH)
        r1=(priceCloseingFList[i]-priceOpeningFList[i])/priceCloseingFList[i-1]
        rSH=(shPriceCloseingFList[indexSH]-shPriceOpeningFList[indexSH])/shPriceCloseingFList[indexSH-1]
        synFList.append(r1/rSH)
        line=dateStrSH+"\t"+str(rSH)+"\t"+str(r1)+"\t"+ str(round(r1/rSH,2))
        fileWrited.write(line+'\n')
    fileWrited.close()
    print("大盘同步性分析写入"+synFile)
    

    

def highAndlowPrice(stockID,daysList):
    for days in daysList:
        print("-"*50)
        print("分析周期(交易日/天):\t"+str(days)+"\t起始日期:"+dateStrList[-days]+"\t结束日期:"+dateStrList[-1])
        
        priceHighest=max(priceHighestFList[-days:-1])
        datePriceHighest=getDateOfPrice(priceHighest,priceHighestFList,dateStrList)
        print("区间内最高价:\t"+str(priceHighest)+"\t出现日期:\t"+datePriceHighest)
        
        priceLowest=min(priceLowestFList[-days:-1])
        datePriceLowest=getDateOfPrice(priceLowest,priceLowestFList,dateStrList)
        print("区间内最低价:\t"+str(priceLowest)+"\t出现日期:\t"+datePriceLowest)

        natureDaysNumFromLastPeak2Today=-1  
        if datePriceHighest>=datePriceLowest:
            natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceHighest)
        else:
            natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceLowest)
        print("上个最值距离今天的自然日个数(天):\t"+str(natureDaysNumFromLastPeak2Today.days))
        print("最高点出现与最低点出现交易日个数(天):\t"+str(1+priceHighestFList.index(priceHighest)-priceLowestFList.index(priceLowest)))
        daySpan=calNatureDays(datePriceHighest,datePriceLowest)
        print("最高点出现与最低点出现自然日个数(天):\t"+str(daySpan))
        print("最高点/最低点:\t"+str(round(priceHighest/priceLowest,2)))

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    goalFilePath='result.txt'
    dataPath=u"dataStock"

    iDaysPeriodUser=300
    readStockSH999999()
    highAndlowPriceSH(iDaysPeriodUser)
    print ("正在进行大盘时空分析：")
    findPeak(30) 
    findPeak(50)
    findPeak(100)
    findPeak(200) 

    stockID="002673"
    readStockByID(stockID)
  ##  highAndlowPrice(stockID,[iDaysPeriodUser,30,60,120])
    for item in [iDaysPeriodUser,30,60,120]:
        dateStrStart=dateStrList[-item-1]
        dateStrEnd=dateStrList[-1]
        print("\n"+"$"*80)
        analysisDate(stockID,dateStrStart,dateStrEnd)
        analysisScale(stockID,dateStrStart,dateStrEnd)
        numConsecutiveTradeDays=5
        fScale=0.1
        analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale)

    fileWrited=open(goalFilePath,'w')
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    
    analysisSynchronization(stockID,dateStrList[-100],dateStrList[-1])
    timeSpan=time.clock()-startClock

    print("Time used(s):",round(timeSpan,2))


