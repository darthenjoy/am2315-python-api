from AM2315 import AM2315

sensor=AM2315()
#print(sensor.values())
for i in range (0,5):
  x=sensor.values()
  try:
    if x[0].find("err") > 0:
       next
  except:
    try: 
      if x[0] > 0:
          print(x[0],x[1],x[2])
          break 
    except:
      next
if i > 0 :
  print(i ,"retries needed")
