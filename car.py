import dotenv
import sched, time
import warnings


class Car:
    """
    name: Meni Rotblat
    date: 22-01-2023,
    description: class how generate a single car driving
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
        name: Meni Rotblat
        date: 22-01-2023,
        description:
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
        self.config = dotenv.dotenv_values("C:\Python\paiCharm\Car\.env")
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
        name: Meni Rotblat
        date: 22-01-2023,
        description: turn on the engine car
        input: None
        output: None
        """
        self.engine_up = True

    def drive(self, km):
        """
        name: Meni Rotblat
        date: 22-01-2023,
        description: get km from user, after checking validations: if needs to
                    fuel gas => go to refueling method, else, keep going
        input: km
        output: None
        """
        if self.engine_up is False:
            raise ValueError("engine is down")
        if km < 1:
            raise ValueError("value is not valid")
        if type(km) != int:
            raise TypeError("type of a value is not valid")

        culc_fuel_left = (self.fuel_temp - (km // self.fuel_co))

        if culc_fuel_left < 1:
            self.refueling(abs(culc_fuel_left + (km // self.fuel_co)))
        if culc_fuel_left < 10:
            warnings.warn(f"litter to drive in: {culc_fuel_left}")
        self.km -= km
        if self.fuel_temp - (km // self.fuel_co) > 0:
            self.fuel_temp -= (km // self.fuel_co)
        else:
            warnings.warn("there is no gas")
            self.refueling(self.money // self.cust_per_liter)

    def shift_up(self):
        """
        name: Meni Rotblat
        date: 22-01-2023,
        description: increase gear after check validation
        input: None
        output: None
        """
        if self.gear == 6:
            raise OverflowError("your not able raise to 7 gear")
        else:
            self.gear += 1
            self.kph = self.kph * self.gear

    def shift_down(self):
        """
        name: Meni Rotblat
        date: 22-01-2023,
        description: decrease gear after check validation
        input: None
        output: None
        """
        if self.gear == 0:
            raise OverflowError("your not able bring down to under 0 gear")
        else:
            self.gear -= 1
            self.kph = self.kph * self.gear  # kph take goal off kph (30) and double it as number of gears

    def break_d(self):
        """
        name: Meni Rotblat
        date: 22-01-2023,
        description: stop for driving
        input: None
        output: None
        """
        self.kph = 0
        self.gear = 0

    def get_properties(self):
        """
        name: Meni Rotblat
        date: 22-01-2023,
        description: print selected properties
        input: None
        output: None
        """
        print(f"""
        gear: {self.gear}, km: {self.km}, engine: {self.engine_up}
        fuel: {self.fuel_temp}, money: {self.money} 
""")

    def stop_engine(self):
        """
        name: Meni Rotblat
        date: 22-01-2023,
        description: shutdown the engine
        input: None
        output: None
        """
        self.engine_up = False
        self.gear = 0

    def refueling(self, l):
        """
        name: Meni Rotblat
        date: 22-01-2023,
        description: refueling gas after make sure that we have money for that and validation
        input: l, litters we want to fuel
        output: None
        """
        if type(l) != int:  # make suer that l is int
            raise TypeError("value needs to be a integer number type")
        if self.money < 1:  # make sure that we have enough money
            raise ValueError("There is no money")
        if l > 50:  # make sure that we don't jump upper fuel capacity
            raise ValueError("your fuel is up to 50 litter capacity")
        elif l < 1:  # make sure that we don't jump down from minimum fuel capacity
            raise ValueError("the mount needs to be up to 0")
        if self.money * l < self.money:  # money calculating
            raise ValueError("there is no money for this ride ")
        if self.fuel_capacity <= (self.fuel_temp + l):  # fuel capacity calculating
            self.fuel_temp += l
        self.money -= (l * self.cust_per_liter)
