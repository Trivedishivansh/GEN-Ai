device_status = "close"
temprature = 37

if device_status == 'active':
  if temprature >35:
    print("Warning!high temp alert")
  else:
    print("Temp is normal")

else:
  print("Device is offline")