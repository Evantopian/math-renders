
#Imports
import math
import statistics
import numpy as np
import matplotlib.pyplot as plt

def ComputerOutput(topic,m,):
  print('GR:',str(round(((topic[47] - topic[0])/topic[0]),4) * 100) + '%\n')
  standardDeviation = round(statistics.stdev(topic),4)
  Mean = round(statistics.mean(topic),4)
  Correlation = np.corrcoef(topic,months)
  rSquared = math.sqrt(abs(Correlation[0][1]))
  print ('Output:','\nSx:',standardDeviation,'\nx̅:',Mean,'\nr:',round(Correlation[0][1],4),'\nr²:', round(rSquared,4))


months = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]

area = np.pi*3

#//////////////////////////////////////////////////////////////////////////
#Amazon Stocks
#//////////////////////////////////////////////////////////////////////////
AmaStock = open("DataSetsPro/Amazon/AmazonCSV/AmazonStock.txt").readlines()
AmaStock[:] = [line.rstrip('\n') for line in AmaStock]
AmaStock = list(map(float, AmaStock))

colors = ('green')

plt.scatter(months, AmaStock, s=area, c=colors, alpha= 0.5)
plt.title('Amazon Stocks by Months')
plt.xlabel('Months (May 2015 - May 2019)')
plt.ylabel('Amazon Opening Stock Price')
plt.show()
plt.savefig('DataSetsPro/Amazon/AmazonGraphs/AmazonStocksG.png')
plt.clf()

ComputerOutput(AmaStock,months)
#//////////////////////////////////////////////////////////////////////////
#Amazon Volume
#//////////////////////////////////////////////////////////////////////////
AmaVol = open("DataSetsPro/Amazon/AmazonCSV/AmazonVolume.txt").readlines()
AmaVol[:] = [line.rstrip('\n') for line in AmaVol]
AmaVol = list(map(int, AmaVol))

colors = ('red')

plt.scatter(months, AmaVol, s=area, c=colors, alpha= 0.5)
plt.title('Amazon Volumes by Months')
plt.xlabel('Months (May 2015 - May 2019)')
plt.ylabel('Amazon Volume')
plt.show()
plt.savefig('DataSetsPro/Amazon/AmazonGraphs/AmazonVolumeG.png')
plt.clf() 

ComputerOutput(AmaVol,months)


#========================================================================
#========================================================================
#========================================================================


#-------------------------------------------------------------------------
#Barnes and Nobles Stocks
#-------------------------------------------------------------------------
BNStock = open("DataSetsPro/B&N/B&NCSV/B&NStock.txt").readlines()
BNStock[:] = [line.rstrip('\n') for line in BNStock]
BNStock = list(map(float, BNStock))

colors = ('purple')

plt.scatter(months, BNStock, s=area, c=colors, alpha= 0.5)
plt.title('Barnes & Nobles Stocks by Months')
plt.xlabel('Months (May 2015 - May 2019)')
plt.ylabel('Barnes & Nobles Opening Stock Price')
plt.show()
plt.savefig('DataSetsPro/B&N/B&NGraphs/B&NStocksG.png')
plt.clf() 

ComputerOutput(BNStock,months)

#-------------------------------------------------------------------------
#Barnes and Nobles Volumes
#-------------------------------------------------------------------------
BNvol = open("DataSetsPro/B&N/B&NCSV/B&NVolume.txt").readlines()
BNvol[:] = [line.rstrip('\n') for line in BNvol]
BNvol = list(map(int, BNvol))

colors = ('orange')

plt.scatter(months, BNvol, s=area, c=colors, alpha= 0.5)
plt.title('Barnes & Nobles Volumes by Months')
plt.xlabel('Months (May 2015 - May 2019)')
plt.ylabel('Barnes & Nobles Volumes')
plt.show()
plt.savefig('DataSetsPro/B&N/B&NGraphs/B&NVolumeG.png')
plt.clf() 

ComputerOutput(BNvol,months)




