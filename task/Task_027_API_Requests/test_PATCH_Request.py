import pytest
import requests
import allure

base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

@allure.title("Update Request")
@pytest.mark.update
def test_get_token():
    path_url = "/auth"
    full_url = base_url + path_url
    json_payload_auth= {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(full_url, headers= headers, json=json_payload_auth)
    assert response.status_code == 200

    response_json = response.json()
    token = response_json["token"]
    print("Token = ",token)
    assert type(token) == str
    assert len(token) > 0
    return token

@allure.title("Create_and_get_booking_id")
@pytest.mark.update
def test_Create_and_get_booking_id():
    path_url = "/booking"
    full_url = base_url + path_url

    booking_Details_json = {
        "firstname": "Test",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=full_url, headers= headers, json= booking_Details_json )
    response_json = response.json()
    id = response_json["bookingid"]
    print("Booking ID = ",id)
    return id

def test_update_booking_details():
    token1 = test_get_token()
    bookingid = test_Create_and_get_booking_id()
    path_url = "/booking/" + str(bookingid)
    full_url = base_url + path_url

    cookie = 'token=' + token1
    print("Booking id for update: ", bookingid)

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }

    booking_Details_json = {
        "firstname": "Prashant",
        "lastname": "Browne",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-12-01"
        },
        "additionalneeds": "Breakfast & Dinner "
    }

    response = requests.patch(url=full_url, headers= headers, json=booking_Details_json)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["firstname"] == "Prashant"
    assert response_json["lastname"] == "Browne"
    assert response_json["totalprice"] == 250
    assert response_json["depositpaid"] == True
    assert response_json["bookingdates"]["checkin"] == "2025-01-01"
    assert response_json["bookingdates"]["checkout"] == "2025-12-01"
    assert response_json["additionalneeds"] == "Breakfast & Dinner "

    print(booking_Details_json)