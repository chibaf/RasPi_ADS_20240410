import ADS1256
from datetime import date
import time
import matplotlib.pyplot as plt
import serial

from read_m52_class import m5logger2
from ads1256b_class import read_ads1256

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="SL_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

ser0 = serial.Serial("/dev/ttyACM0",19200)
ser1 = serial.Serial("/dev/ttyACM1",19200)
ser2 = serial.Serial("/dev/ttyACM2",19200)
serm = serial.Serial("/dev/ttyUSB0",19200)
ads1256a=read_ads1256()
ads1256b=read_ads1256()
ads1256c=read_ads1256()
sport=m5logger2()

data1=[0]*24
data01=[data1]*10
data2=[0]*10
data02=[data2]*10

while True:
 data=[[],[],[]]
 try:
  ttime=time.time()-start
  if ttime<0.001:
    ttime=0.0
  st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
  ss=str(time.time()-int(time.time()))
  rttime=round(ttime,2)
  temp0=ads1256a.read(ser0)
  temp1=ads1256b.read(ser1)
  temp2=ads1256c.read(ser2)
  data[int(temp0[0])-1]=temp0[1:]
  data[int(temp1[0])-1]=temp1[1:]
  data[int(temp2[0])-1]=temp2[1:]
  array=data[0]+data[1]+data[2]
  array2=sport.read_logger(serm)
  outst=st+ss[1:5]+","+str(rttime)+","
  for i in range(0,len(array)):
    outst=outst+str(array[i])+","
  for i in range(0,len(array2)-1):
    outst=outst+str(array2[i])+","
  outst=outst+str(array2[len(array2)-1])
  outst=outst+"\n"
  print(outst)
  f.write(outst)
  print(len(array))
  print(len(array2))

  data01.pop(-1)
  data02.pop(-1)
  data01.insert(0,array)
#  print(data01)
  data2.insert(0,array2)
#  print(data02)
#  exit()
  rez = [[data01[j][i] for j in range(len(data01))] for i in range(len(data01[0]))]
  rez2 = [[data02[j][i] for j in range(len(data02))] for i in range(len(data02[0]))]
  print(len(rez))
  print(len(rez2))
  x=range(0, 10, 1)
  plt.figure(100)
  plt.clf()
  plt.ylim(-1.0,10.0)
  lin0,=plt.plot(x,rez[0],label="A0")
  lin1,=plt.plot(x,rez[1],label="A1")
  lin2,=plt.plot(x,rez[2],label="A2")
  lin3,=plt.plot(x,rez[3],label="A3")
  lin4,=plt.plot(x,rez[4],label="A4")
  lin5,=plt.plot(x,rez[5],label="A5")
  lin6,=plt.plot(x,rez[6],label="A6")
  lin7,=plt.plot(x,rez[7],label="A7")
  plt.legend(handles=[lin0,lin1,lin2,lin3,lin4,lin5,lin6,lin7])
  plt.pause(0.1)
  plt.figure(200)
  plt.clf()
  plt.ylim(-40,40)
  tl0,=plt.plot(x,rez2[0],label="T0")
  tl1,=plt.plot(x,rez2[1],label="T1")
  tl2,=plt.plot(x,rez2[2],label="T2")
  tl3,=plt.plot(x,rez2[3],label="T3")
  tl4,=plt.plot(x,rez2[4],label="T4")
  tl5,=plt.plot(x,rez2[5],label="T5")
  tl6,=plt.plot(x,rez2[6],label="T6")
  tl7,=plt.plot(x,rez2[7],label="T7")
  tl8,=plt.plot(x,rez2[8],label="T8")
  tl9,=plt.plot(x,rez2[9],label="T9")
  plt.legend(handles=[tl0,tl1,tl2,tl3,tl4,tl5,tl6,tl7,tl8,tl9])
  plt.pause(0.1)
 except KeyboardInterrupt:
  f.close()
  ser0.close()
  ser1.close()
  ser2.close()
  serm.close()
  exit()
