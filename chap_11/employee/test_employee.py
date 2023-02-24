from employee import Employee
import pytest


@pytest.fixture
def employee():
    employee = Employee('nguyen', 'tran', 5000)
    return employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert 10000 == employee.salary


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert 15000 == employee.salary
