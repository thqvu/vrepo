### Calculate EIRP Classic Mode metric
from os import system

# system('cls')

### Input Bandwidth
BW = input('Enter the min Bandwidth along the path in Kbps: ')
BW = int(BW)
BW = 10000000 // BW
print('The Bandwidth value = ' + str(BW))

### Input Delay
DLY = input('Enter the cumulative Delay in microseconds: ')
DLY = int(DLY)
DLY = DLY // 10
print('The Delay value = ' + str(DLY))

COMP_METRIC = (BW + DLY) * 256
print('EIGRP Classic Mode metric = ' + str(COMP_METRIC))
