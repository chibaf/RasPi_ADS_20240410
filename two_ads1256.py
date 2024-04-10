from datetime import date
import time
import matplotlib.pyplot as plt
import serial

from ads1256b_class import read_ads1256

ser0 = serial.Serial("/dev/ttyACM0",19200)
ser1 = serial.Serial("/dev/ttyACM1",19200)

ads1256a=read_ads1256()
ads1256b=read_ads1256()

while True:
  temp0=ads1256a.read(ser0)
  temp1=ads1256b.read(ser1)
  if temp0[0]==1.0:
    data1=temp0[1:]
  else:
    data1=temp1[1:]
  if temp1[0]==2.0:
    data2=temp1[1:]
  else:
    data2=temp0[1:]
  data1.extend(data2)
  print(len(data1))
  print(data1)