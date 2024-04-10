from datetime import date
import time
import matplotlib.pyplot as plt
import serial

from ads1256b_class import read_ads1256

ser0 = serial.Serial("/dev/ttyACM0",19200)
ser1 = serial.Serial("/dev/ttyACM1",19200)
ser2 = serial.Serial("/dev/ttyACM2",19200)

ads1256a=read_ads1256()
ads1256b=read_ads1256()
ads1256c=read_ads1256()

data=[[],[],[]]
while True:
  temp0=ads1256a.read(ser0)
  temp1=ads1256b.read(ser1)
  temp2=ads1256c.read(ser2)
  data[int(temp0[0])-1]=temp0[1:]
  data[int(temp1[0])-1]=temp1[1:]
  data[int(temp2[0])-1]=temp2[1:]
  data1=data[0]+data[1]+data[2]
  print(data1)