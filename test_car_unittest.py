import unittest

import dotenv
from dotenv import dotenv_values
from Car.car import Car
from Car.exceptions_loging import Exceptions_logs


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: initial test page  \n
            input:
            output:
            :return:
        """
        self.car = Car()
        self.exc = Exceptions_logs()
        self.config = dotenv_values(dotenv_path=dotenv.find_dotenv(".env"))

    def test_start_engine(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: testing start engine func, so that engine up params changed \n
        """
        try:
            self.car.start_engine()  # start angine
            self.assertEqual(self.car.engine_up, True)
            self.exc.send(self.config["TEST_PASS"].format("test_start_engine,", "engine_up"))
        except Exception as e:
            self.exc.send(
                self.config["TEST_FAIL"].format(f"test_start_engine,\n", "engine_up\n", e))
        except AssertionError as ae:
            self.exc.send(
                self.config["ASSERT_FAIL"].format(f"test_start_engine,\n", "engine_up\n", ae))

    def test_stop_engine(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: test start/stop engine and the gear that change  \n
        """
        try:
            self.car.start_engine()  # test that after start and verify that, we stop the engine, and is down
            self.assertEqual(self.car.engine_up, True)
            self.car.stop_engine()
            self.assertEqual(self.car.engine_up, False)

            self.car.gear = 30  # test that gear is change
            self.assertEqual(self.car.gear, 30)
            self.car.stop_engine()
            self.assertEqual(self.car.gear, 0)

            self.exc.send(self.config["TEST_PASS"].format("stop_engine", "engine_up"))
        except Exception as e:
            self.exc.send(
                self.config["TEST_FAIL"].format(f"stop_engine,\n", "engine_up\n", e))
        except AssertionError as ae:
            self.exc.send(self.config["ASSERT_FAIL"].format(f"stop_engine,\n", "engine_up,\n", ae))

    def test_shift_up(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: test shifting up overflow  \n
        """
        try:
            with self.assertRaises(OverflowError):  # try to  get an error in 7 times upload gear
                for i in range(7):
                    self.car.shift_up()
            self.exc.send(self.config["TEST_PASS"].format("shift_up\n,", "raise except OverflowError\n"))
        except Exception as e:
            self.exc.send(
                self.config["TEST_FAIL"].format(f"shift_up,\n", "raise except OverflowError\n", e))
        except AssertionError as ae:
            self.exc.send(self.config["ASSERT_FAIL"].format(f"shift_up,\n", "raise except OverflowError\n", ae))

    def test_shift_down(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: test shifting down overflow and changes  \n
        """
        try:
            with self.assertRaises(OverflowError):  # try to get an error in 7 times bring down gear
                self.car.shift_down()

            self.car.shift_up()
            self.car.shift_up()
            self.car.shift_down()

            self.assertEqual(self.car.gear, 1)  # try to exception by upper the gear to 2 and down it to 1 by shift_down
            self.exc.send(
                self.config["TEST_PASS"].format("shift_down\n,", "raise except OverflowError, gear, shift_up\n"))
        except Exception as e:
            self.exc.send(
                self.config["TEST_FAIL"].format(f"shift_down,\n", "raise except OverflowError, gear, shift_up\n", e))
        except AssertionError as ae:
            self.exc.send(
                self.config["ASSERT_FAIL"].format(f"shift_down,\n", "raise except OverflowError, gear, shift_up\n", ae))

    def test_break_d(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: test shifting up overflow  \n
        """
        try:
            self.car.kph = 60  # initialize kph for the test and check if they are offset right
            self.assertEqual(self.car.kph, 60)
            self.car.gear = 2  # same on gear
            self.assertEqual(self.car.gear, 2)

            self.car.break_d()
            self.assertEqual(self.car.kph, 0)  # test that kpa equal to 0
            self.assertEqual(self.car.gear, 0)  # test that gear equal to 0

            self.exc.send(self.config["TEST_PASS"].format("break_d\n,", ("kph", f"gear\n")))
        except Exception as e:
            self.exc.send(self.config["TEST_FAIL"].format("break_d,\n", ("kph", "gear"), f"\n{e}"))
        except AssertionError as ae:
            self.exc.send(
                self.config["ASSERT_FAIL"].format(f"break_d,\n", ("kph", "gear"), f" \n{ae}"))

    def test_get_properties(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: test getting properties, type  \n
        """
        try:
            self.assertEqual(self.car.get_properties(), print())  # test that method printed
            self.exc.send(self.config["TEST_PASS"].format("get_properties\n,", "get_properties"))
        except Exception as e:
            self.exc.send(self.config["TEST_FAIL"].format("get_properties,\n", "get_properties", f"\n{e}"))
        except AssertionError as ae:
            self.exc.send(self.config["ASSERT_FAIL"].format(f"get_properties,\n", "get_properties", f" \n{ae}"))

    def test_refueling(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: test refueling abilities: catching raises Values Error and type error\n
        """
        try:
            with self.assertRaises(ValueError):
                self.car.refueling(0)
            with self.assertRaises(ValueError):
                self.car.refueling(51)
            with self.assertRaises(TypeError):
                self.car.refueling("n")
            with self.assertRaises(ValueError):
                self.car.refueling(1050)
            self.exc.send(self.config["TEST_PASS"].format("refueling", "raise"))
        except Exception as e:
            self.exc.send(
                self.config["TEST_FAIL"].format(f"refueling,\n", "raise\n", e))
        except AssertionError as ae:
            self.exc.send(self.config["ASSERT_FAIL"].format(f"refueling,\n", "raise,\n", ae))

    def test_drive(self):
        """
            Name: Meni Rotblat.\n
            Date: 22-01-2023. \n
            Description: test driving, error raises  \n
        """
        try:
            self.car.drive(5)  # test driving that km is up
            self.assertEqual(self.car.km, 45)  # km is initial with 50
            with self.assertRaises(ValueError):  # test raise when engine shutdown
                self.car.engine_up = False
                self.car.drive(5)
            with self.assertRaises(ValueError):  # test raise when km < 1
                self.car.drive(0)
            with self.assertRaises(TypeError):  # test valid input value
                self.car.refueling("n")
            self.exc.send(self.config["TEST_PASS"].format("drive", "raise"))
        except Exception as e:
            self.exc.send(
                self.config["TEST_FAIL"].format(f"drive,\n", "raise\n", e))
        except AssertionError as ae:
            self.exc.send(self.config["ASSERT_FAIL"].format(f"drive,\n", "raise,\n", ae))


if __name__ == '__main__':
    unittest.main()
