from AM2315 import AM2315
MAXTRIES = 5
sensor=AM2315()
for i in range (0,MAXTRIES):
  x = sensor.values()
  if x[2] != 0:
     next
#  if (x[0] > 0 and x[1] != 0) or (x[0]>0 and i>MAXTRIES-1) :
  print(x[0],x[1],x[2])
  break
#if i > 0 :
#  print(i ,"retries needed")

