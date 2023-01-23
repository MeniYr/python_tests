import dotenv
import pytest
from Car.car import Car
from Car.exceptions_loging import Exceptions_logs
from dotenv import dotenv_values
import os
config = dotenv_values(dotenv_path=dotenv.find_dotenv(".env"))
exc = Exceptions_logs()


@pytest.fixture
def car():
    return Car()


@pytest.mark.start_engine
def test_start_engine(car):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: testing start engine func, so that engine up params changed \n
    :param car:
    :return:
    """
    try:
        car.start_engine()  # start angine
        assert car.engine_up is True  # checking that the engine is up
        exc.send(config["TEST_PASS"].format("test_start_engine,", "engine_up"))
    except Exception as e:
        exc.send(
            config["TEST_FAIL"].format(f"test_start_engine,\n", "engine_up\n", e))
    except AssertionError as ae:
        exc.send(
            config["ASSERT_FAIL"].format(f"test_start_engine,\n", "engine_up\n", ae))


@pytest.mark.stop_engine
def test_stop_engine(car):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: test start/stop engine and the gear that change  \n
    :param car:
    :return:
    """
    try:
        car.start_engine()  # test that after start, and verify that, we stop the engine, and is down
        assert car.engine_up is True
        car.stop_engine()
        assert car.engine_up is False

        car.gear = 30  # test that gear is change
        assert car.gear == 30
        car.stop_engine()
        assert car.gear == 0

        exc.send(config["TEST_PASS"].format("stop_engine", "engine_up"))
    except Exception as e:
        exc.send(
            config["TEST_FAIL"].format(f"stop_engine,\n", "engine_up\n", e))
    except AssertionError as ae:
        exc.send(config["ASSERT_FAIL"].format(f"stop_engine,\n", "engine_up,\n", ae))


@pytest.mark.shift_up
def test_shift_up(car):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: test shifting up overflow  \n
    :param car:
    :return:
    """
    try:
        with pytest.raises(OverflowError):  # try to  get an error in 7 times upload gear
            for i in range(7):
                car.shift_up()
        exc.send(config["TEST_PASS"].format("shift_up\n,", "raise except OverflowError\n"))
    except Exception as e:
        exc.send(
            config["TEST_FAIL"].format(f"shift_up,\n", "raise except OverflowError\n", e))
    except AssertionError as ae:
        exc.send(config["ASSERT_FAIL"].format(f"shift_up,\n", "raise except OverflowError\n", ae))


@pytest.mark.shift_down
def test_shift_down(car):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: test shifting down overflow and changes  \n
    :param car:
    :return:
    """
    try:
        with pytest.raises(OverflowError):  # try to get an error in 7 times bring down gear
            car.shift_down()
        car.shift_up()
        car.shift_up()
        car.shift_down()

        assert car.gear == 1  # try to exception by upper the gear to 2 and down it to 1 by shift_down
        exc.send(
            config["TEST_PASS"].format("shift_down\n,", "raise except OverflowError, gear, shift_up\n"))
    except Exception as e:
        exc.send(
            config["TEST_FAIL"].format(f"shift_down,\n", "raise except OverflowError, gear, shift_up\n", e))
    except AssertionError as ae:
        exc.send(
            config["ASSERT_FAIL"].format(f"shift_down,\n", "raise except OverflowError, gear, shift_up\n", ae))


@pytest.mark.break_d
def test_break_d(car):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: test shifting up overflow  \n
    :param car:
    :return:
    """
    try:
        car.kph = 60  # initialize kph for the test and check if they are offset right
        assert car.kph == 60
        car.gear = 2  # same on gear
        assert car.gear == 2

        car.break_d()
        assert car.kph == 0  # test that kpa equal to 0
        assert car.gear == 0  # test that gear equal to 0

        exc.send(config["TEST_PASS"].format("break_d\n,", ("kph", f"gear\n")))
    except Exception as e:
        exc.send(config["TEST_FAIL"].format("break_d,\n", ("kph", "gear"), f"\n{e}"))
    except AssertionError as ae:
        exc.send(
            config["ASSERT_FAIL"].format(f"break_d,\n", ("kph", "gear"), f" \n{ae}"))


@pytest.mark.get_properties
@pytest.mark.skip
def test_get_properties(car):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: test getting properties, type  \n
    :param car:
    :return:
    """
    try:
        assert car.get_properties() is None  # test that method printed
        exc.send(config["TEST_PASS"].format("get_properties\n,", "get_properties"))
    except Exception as e:
        exc.send(config["TEST_FAIL"].format("get_properties,\n", "get_properties", f"\n{e}"))
    except AssertionError as ae:
        exc.send(config["ASSERT_FAIL"].format(f"get_properties,\n", "get_properties", f" \n{ae}"))


@pytest.mark.test_refueling
@pytest.mark.parametrize("l", [-1, 51, 1050])
def test_refueling(car, l):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: test refueling abilities: catching raises Values Error and type error\n
    :param car:
    :return:
    """
    try:

        with pytest.raises(ValueError):
            car.refueling(l)
        with pytest.raises(TypeError):
            car.refueling("n")
        exc.send(config["TEST_PASS"].format("refueling", "raise"))
    except Exception as e:
        exc.send(
            config["TEST_FAIL"].format(f"refueling,\n", "raise\n", e))
    except AssertionError as ae:
        exc.send(config["ASSERT_FAIL"].format(f"refueling,\n", "raise,\n", ae))


@pytest.mark.drive
def test_drive(car):
    """
    Name: Meni Rotblat.\n
    Date: 22-01-2023. \n
    Description: test driving, error raises  \n
    :param car:
    :return:
    """
    try:
        car.engine_up = True
        car.drive(5)  # test driving that km is up
        assert car.km == 995  # km is initial with 50
        with pytest.raises(ValueError):  # test raise when engine shutdown
            car.engine_up = False
            car.drive(5)
        with pytest.raises(ValueError):  # test raise when km < 1
            car.drive(0)
        with pytest.raises(ValueError):  # test valid input value
            car.drive("n")
        exc.send(config["TEST_PASS"].format("drive", "raise"))
    except Exception as e:
        exc.send(
            config["TEST_FAIL"].format(f"drive,\n", "raise\n", e))
    except AssertionError as ae:
        exc.send(config["ASSERT_FAIL"].format(f"drive,\n", "raise,\n", ae))
