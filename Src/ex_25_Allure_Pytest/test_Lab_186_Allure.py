import pytest
import allure

@allure.title("Verify that the create booking is working")
@allure.description("We are going to verify the create booking in the future of this function")
@pytest.mark.positive
def test_create_booking_positive():
    print("test_create_booking_positive")
    assert 1-1==2

@allure.title("Verify that the create booking with invalid data is working")
@allure.description("This test case to check the negative create booking function")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("create_booking_negative_1")
    assert 1+1==2


@allure.title("Verify that the create booking with invalid data is working")
@allure.description("This test case to check the negative create booking function")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("create_booking_negative_2")
    assert 1+1==2
