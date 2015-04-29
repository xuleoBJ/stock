# -*- coding: utf-8 -*- 
import os
import shutil

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

def printDateOfPrice(price,priceFList,dateStrList):
    indexPrice=priceFList.index(price)
    print "出现日期:\t"+dateStrList[indexPrice]


def highAndlowPriceSH(days):
    print "分析周期(交易日/天):\t"+str(days)+"\t起始日期:"+shDateStrList[-days]
    priceHighest=max(shPriceHighestFList[-days:-1])
    print "区间内最高点:\t"+str(priceHighest)
  ##  print "date of Price:\t"+shDateStrList[shPriceHighestFList.index(priceHighest)]
    printDateOfPrice(priceHighest,shPriceHighestFList,shDateStrList)

    priceLowest=min(shPriceLowestFList[-days:-1])
    print "区间内最低点:\t"+str(priceLowest)
    printDateOfPrice(priceLowest,shPriceLowestFList,shDateStrList)

    print "最高点/最低点:\t"+str(round(priceHighest/priceLowest,2))


def highAndlowPrice(days):
    print "#"*50
    print "分析周期(交易日/天):\t"+str(days)+"\t起始日期:"+dateStrList[-days]
    priceHighest=max(priceHighestFList[-days:-1])
    print "区间内最高价:\t"+str(priceHighest)
    
    priceLowest=min(priceLowestFList[-days:-1])
    print "区间内最低价:\t"+str(priceLowest)
    print "最高点/最低点:\t"+str(round(priceHighest/priceLowest,2))

if __name__=="__main__":

    goalDirPath='result.txt'
    sourcePath=u"C:\new_dxzq_v6\vipdoc\sh\lday"

    lineIndex=0
    fileSHOpened= open('999999'+'.txt','r')
    print "-"*50
    print "current analysy:"+"sh999999"
    for line in fileSHOpened.readlines():
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
    fileSHOpened.close()
    highAndlowPriceSH(400)

    print "-"*50
    print "current analysy:"+"600196"
    stockID='600196'+'.txt'
    stockFile=os.path.join(sourcePath,stockID)

    fileOpened=open(stockID,'r')
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
    iStartNum=0
    iEndNum=len(dateStrList)


    highAndlowPrice(300)
    highAndlowPrice(30)
    highAndlowPrice(60)
    highAndlowPrice(120)
    for i in range(-30,0):
        pass

    fileWrited=open(goalDirPath,'w')
##  lineList=[]
##    for i in range(0,len(lineList)-1):
##        splitLine=lineList[i].split()
##        splitNextLine=lineList[i+1].split()
##        if len(splitLine)!=4:
##            print i,line
##        else:
##            fileWrited.write('\t'.join(splitLine)+'\n')
##            if splitNextLine[0]!=splitLine[0]:
##                splitLine[1]=str(int(splitLine[1])+1)
##                splitLine[2]=splitLine[3]
##                fileWrited.write('\t'.join(splitLine)+'\n')
##            
##    fileWrited.write(lineList[-1])
##    splitLine=lineList[-1].split()
##    splitLine[1]=str(int(splitLine[1])+1)
##    splitLine[2]=splitLine[3]
##    fileWrited.write('\t'.join(splitLine)+'\n')
    
    fileWrited.close()




