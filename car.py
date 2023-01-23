import dotenv
import sched, time
import warnings


class Car:
    """
    name: Meni Rotblat\n
    date: 22-01-2023,\n
    description: class how generate a single car driving\n
    :parameter
        init:
            s - time object
            config - search on env file as a dict
            fuel_co - Fuel consumption, init with 20
            money - for purchase gas, init with 500
            cust_per_liter - init with 10
            gear - for manage shift up and down, init with 0
            engine_up - bool, init with False
            kph - unit of speed, init with 0
            km - distance, init with 0
            gear_mph_limit - init with 30
            fuel_capacity - init with 50
            fuel_temp - init with 0, use for scale up and down temporary
        methods:
            start_engine - start engine
            drive - start drive
            shift_up - increase gear
            shift_down - decrease geare
            break_d - stop driving
            get_properties - print selected properties
            stop_engine - turn off
            refueling - fuelling gas
    """

    def __init__(self):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description:\n
        :parameter
        init:
        self.s =
        self.config =
        self.fuel_co =
        self.money =
        self.cust_per_liter =
        self.gear =
        self.car_shutdown =
        self.engine_up =
        self.mph =
        self.gear_mph_limit =
        self.fuel_capacity =
        self.mph_temp =
        self.fuel_temp =
        """
        self.s = sched.scheduler(time.time, time.sleep)
        self.config = dotenv.dotenv_values(dotenv_path=dotenv.find_dotenv(".env"))
        self.fuel_co = int(self.config["FUEL_CO"])
        self.money = int(self.config["MONEY"])
        self.cust_per_liter = int(self.config["CUST_PER_LITER"])
        self.gear = int(self.config["GEAR"])
        self.engine_up = False
        self.kph = 0
        self.km = int(self.config["FUEL_CAPACITY"]) * int(self.config["FUEL_CO"])
        self.gear_mph_limit = int(self.config["GEAR_MPH_LIMIT"])
        self.fuel_capacity = int(self.config["FUEL_CAPACITY"])
        self.fuel_temp = int(self.config["FUEL_CAPACITY"])

    def start_engine(self):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: turn on the engine car\n
        input: None
        output: None
        """
        self.engine_up = True

    def drive(self, km):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: get km from user, after checking validations: if needs to
                    fuel gas => go to refueling method, else, keep going\n
        input: km\n
        output: None
        """
        if self.engine_up is False:
            raise ValueError(self.config["VALUE_ERR_DRIVE1"])
        if km < 0:
            raise ValueError(self.config["VALUE_ERR_DRIVE2"])
        if type(km) != int:
            raise TypeError(self.config["TYPE_ERR_DRIVE"])

        culc_fuel_left = (self.fuel_temp - (km // self.fuel_co))

        if culc_fuel_left < 1:
            self.refueling(abs(culc_fuel_left + (km // self.fuel_co)))
        if 10 > culc_fuel_left > 0:
            warnings.warn(f'{self.config["WARNINGS_WARN_DRIVE"]} {culc_fuel_left}')
        self.km -= km
        if self.fuel_temp - (km // self.fuel_co) > 0:
            self.fuel_temp -= (km // self.fuel_co)
        else:
            warnings.warn("there is no gas")
            self.refueling(self.money // self.cust_per_liter)

    def shift_up(self):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: increase gear after check validation\n
        input: None\n
        output: None
        """
        if self.gear == 6:
            raise OverflowError(self.config["OVER_FLOW_ERROR_SHIFT_UP"])
        else:
            self.gear += 1
            self.kph = self.kph * self.gear

    def shift_down(self):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: decrease gear after check validation\n
        input: None\n
        output: None
        """
        if self.gear == 0:
            raise OverflowError(self.config["OVER_FLOW_ERROR_SHIFT_DOWN"])
        else:
            self.gear -= 1
            self.kph = self.kph * self.gear  # kph take goal off kph (30) and double it as number of gears

    def break_d(self):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: stop for driving\n
        input: None\n
        output: None
        """
        self.kph = 0
        self.gear = 0

    def get_properties(self):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: print selected properties\n
        input: None\n
        output: None
        """
        print(f"""
        gear: {self.gear}, km: {self.km}, engine: {self.engine_up}
        fuel: {self.fuel_temp}, money: {self.money} 
""")

    def stop_engine(self):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: shutdown the engine\n
        input: None\n
        output: None
        """
        self.engine_up = False
        self.gear = 0

    def refueling(self, l):
        """
        name: Meni Rotblat\n
        date: 22-01-2023,\n
        description: refueling gas after make sure that we have money for that and validation\n
        input: l, litters we want to fuel\n
        output: None
        """
        if type(l) != int:  # make suer that l is int
            raise TypeError(self.config["TYPE_ERR_REFUELING"])
        if self.money < 1:  # make sure that we have enough money
            raise ValueError(self.config["VALUE_ERR_REFUELING1"])
        if l > self.fuel_capacity:  # make sure that we don't jump upper fuel capacity
            raise ValueError(self.config["VALUE_ERR_REFUELING2"])
        elif l < 1:  # make sure that we don't jump down from minimum fuel capacity
            raise ValueError(self.config["VALUE_ERR_REFUELING3"])
        if self.money * l < self.money:  # money calculating
            raise ValueError(self.config["VALUE_ERR_REFUELING4"])
        if self.fuel_capacity <= (self.fuel_temp + l):  # fuel capacity calculating
            self.fuel_temp += l
            self.km += (l * self.fuel_co)
        self.money -= (l * self.cust_per_liter)
