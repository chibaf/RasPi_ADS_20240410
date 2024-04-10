from read_shield_class import Shield
import time
import ADS1256

shield=Shield()
while True:
  adcv=shield.read_shield()
  #print(adcv[1])       #pressure
  a=float(adcv[0])
  a0=0.011352301997220754
  b=(a-a0)/a0
  mm=10.0*100*10 #height of water for 1atm
  s=f"""{b:.6},   {b*mm:.2}mm"""
  print(s)
  time.sleep(1.0)
exit()
