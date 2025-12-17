import pytest
import allure
import requests

@allure.title("Verify the get request")
@allure.description("Verify that the get request is successful and basically gives the 200 OK as a success code")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code==200

@allure.title("Verify the GET request of restfull booker with invalid ID")
@allure.description("This test case check booking -1 and Verify that the get request is successful and basically gives the 404 as a success code")
@pytest.mark.negative
def test_get_request_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url)
    assert response_data.status_code==404