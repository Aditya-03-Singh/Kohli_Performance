
class Sensor():
    def __init__(self,name,location,record_date):
        self.name=name
        self.location=location
        self.record_date=record_date
        self.data={}

    def add_data(self, data, time):
        self.data["data"]=data
        self.data["time"]=time
        print("Data points added successfully")

    def clear_data(self):
        self.data={}
        print("Data removed successfully")

class accelerometer(Sensor):
    def show_sensor_type(self):
        print(f"This is {self.name}")

acc= accelerometer(
    name="accelerometer",
    location="haldia",
    record_date="2023-01-19"
)

acc.add_data(
    data=acc_data,
    time=acc_time
)
print('Accelerometer data: ',acc.data)

class gyro(accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")

gyro_data = np.random.randint(-15,15,10)
gyro_time = np.arange(10)

gyro = gyro(
    name="gyroscope",
    location="kolkata",
    record_date="2023-01-10"
)

gyro.add_data(time=gyro_time , data=gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()

class GPS(Sensor):
    def __init__(self, name, location ,  record_date , brand):
        super().__init__(
            name, location, record_date 
        )
        self.brand = brand

gps = GPS(
    name="GPS",
    location="Chennai",
    record_date="2023-01-10",
    brand="espressi"
)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)