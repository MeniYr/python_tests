from exceptions_loging import Exceptions_logs
from car import Car

if __name__ == '__main__':

    try:
        car = Car()  # car class
        car.start_engine()
        car.drive(996)
        car.get_properties()
        car.drive(600)
        car.get_properties()
        car.drive(50)
        car.get_properties()
        car.shift_up()
        car.stop_engine()
        car.get_properties()
    except Exception as e:
        exc = Exceptions_logs()  # log manage class
        exc.send(e)
        print(e)
