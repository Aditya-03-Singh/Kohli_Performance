from sensormodel import accelerometer, Gyro, gps
import numpy as np

acc = accelerometer(name="Accelerometer", location="Haldia", record_date="2023-01-10")

gyro = Gyro(
    name="Gyroscope",
    location="Haldia",
    record_date="2023-01-10",
    brand="espressi"
)

gps = Gps(
    name="GPS",
    location="Chennai",
    record_date="2023-10-01",
    brand="espressi"
)

time= np.arrange(10)
acc_data= np.random.randint(-15,15,10)
gps_data= np.random.randit(-12,12,10)

print(acc.name)
print(acc.location)
print(acc.record_date)
acc.add_data(data=acc_data, time=time)

print(gyro.name)
print(gyro.location)
print(gyro.record_date)
gyro.add_data(
    data= gyro_data,
    time=time
)

print(gps.time)
print(gps.location)
print(gps.record_date)
print(gps.brand)

gps.add_data(
    data=gps_data,
    time= time
)