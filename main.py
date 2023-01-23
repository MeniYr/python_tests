import dotenv

from exceptions_loging import Exceptions_logs
from car import Car

if __name__ == '__main__':
    exc = Exceptions_logs()  # log manage class
    config = dotenv.dotenv_values(dotenv_path=dotenv.find_dotenv(".env"))
    try:
        car = Car()  # car class
        car.start_engine()
        car.drive(996)
        car.get_properties()
        car.drive(600)
        car.get_properties()
        car.shift_up()
        car.get_properties()
        car.stop_engine()
        car.get_properties()

    except ValueError as v:
        exc.send(f'{config["MAIN_EXCEPTIONS_VALUE"]} {v}')
        print(f'{config["MAIN_EXCEPTIONS_VALUE"]}  {v}')
    except TypeError as t:
        exc.send(f'{config["MAIN_EXCEPTIONS_TYPE"]} {t}')
        print(f'{config["MAIN_EXCEPTIONS_TYPE"]}  {t}')
    except OverflowError as o:
        exc.send(f'{config["MAIN_EXCEPTIONS_OVER_FLOW"]}  {o}')
        print(f'{config["MAIN_EXCEPTIONS_OVER_FLOW"]}  {o}')
    except Exception as e:
        exc.send(f'{config["MAIN_EXCEPTIONS_GENERAL"]}  {e}')
        print(f'{config["MAIN_EXCEPTIONS_GENERAL"]}  {e}')
