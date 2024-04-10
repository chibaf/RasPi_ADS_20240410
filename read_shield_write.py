from read_shield_class import Shield
import time
import ADS1256
import sys,csv
import numpy as np

shield=Shield()
with open(sys.argv[1], 'a') as record_append:
  while True:
    try:
      adc=shield.read_shield()
      np.savetxt(record_append, np.asarray([adc]), delimiter=',')
      time.sleep(0.5)
    except KeyboardInterrupt:
      break 
exit()
