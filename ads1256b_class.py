class read_ads1256:

  def read(self,ser):
    import serial
    line = ser.readline()
    try:
      line2=line.strip().decode('utf-8')
    except UnicodeDecodeError:
      return [0.0]*9
    data = [str(val) for val in line2.split(",")]
    data1=[]
    if len(data)==9:
      for i in range(0,9):
        try:
          fd=float(data[i])
        except:
          return [0.0]*9
        data1.append(fd)
    else:
      return [0.0]*9
    return data1