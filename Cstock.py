## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy

##��ȡָ������List
class Stock:
    dateStrList=[]
    priceOpeningFList=[]
    priceCloseingFList=[]
    priceHighestFList=[]
    priceLowestFList=[]
    tradeVolumeFList=[] ##�ɽ���
    turnoverFList=[]  ##�ɽ���
    riseRateFList=[]  ##�Ƿ�
    waveRateFList=[] ##�����Ƿ�
    def __init__(self,stockID):
        dirData="export"
        print("#"*80)
        stockDataFile=os.path.join(dirData,stockID+'.txt')
        fileOpened=open(stockDataFile,'r')
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex=lineIndex+1
            splitLine=line.split()
            if lineIndex==1:
                print(line)
            if line!="" and lineIndex>=3 and len(splitLine)>=5:
                self.dateStrList.append(splitLine[0])
                self.priceOpeningFList.append(float(splitLine[1]))
                self.priceHighestFList.append(float(splitLine[2]))
                self.priceLowestFList.append(float(splitLine[3]))
                self.priceCloseingFList.append(float(splitLine[4]))
                self.tradeVolumeFList.append(float(splitLine[5]))
                if len(self.priceCloseingFList)>=2:
                    self.riseRateFList.append(round(100*(self.priceCloseingFList[-1]-self.priceCloseingFList[-2])/self.priceCloseingFList[-1],2))
                    self.waveRateFList.append(round(100*(self.priceHighestFList[-1]-self.priceLowestFList[-2])/self.priceCloseingFList[-1],2))
                else:
                    self.riseRateFList.append(0)
                    self.waveRateFList.append(0)
        fileOpened.close()
        print("���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+self.dateStrList[0]+"\t���ݽ����գ�\t"+self.dateStrList[-1])


class StockSH:   
    shLineList=[]
    shDateStrList=[]
    shPriceOpeningFList=[]
    shPriceCloseingFList=[]
    shPriceHighestFList=[]
    shPriceLowestFList=[]
    shTradeVolumeFList=[]
    shRiseRateFList=[]  ##�Ƿ�
    shWaveRateFLst=[] ##�����Ƿ�
    def __init__(self):
        print("#"*80)
        print ("��ǰ��Ʊ����:"+"sh999999")
        stockDataFile=os.path.join("market",'999999.txt')
        fileOpened=open(stockDataFile,'r')
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex=lineIndex+1
            splitLine=line.split()
            if line!="" and lineIndex>=3 and len(splitLine)>=6:
                self.shLineList.append(line)
                self.shDateStrList.append(splitLine[0])
                self.shPriceOpeningFList.append(float(splitLine[1]))
                self.shPriceHighestFList.append(float(splitLine[2]))
                self.shPriceLowestFList.append(float(splitLine[3]))
                self.shPriceCloseingFList.append(float(splitLine[4]))
                self.shTradeVolumeFList.append(float(splitLine[5]))
        fileOpened.close()
        print("��֤���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+self.shDateStrList[0]+"���ݽ����գ�\t"+self.shDateStrList[-1])
if __name__=="__main__":
    print("\n"+"#"*80)
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    a=Stock('600000') 
    print ("�����������ƣ�")
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
    raw_input()

