data1 = 10      #integer
data2 = 5.7     #float
data3 = "abcd"  #string
data4 = True    #boolean
data5 = complex(5,6)  #complex

#import tipe data dari bahasa c
from ctypes import c_double #contoh c double
dataCDouble = c_double(10.5) 

print("data : ", dataCDouble)
print("tipe : ", type(dataCDouble))