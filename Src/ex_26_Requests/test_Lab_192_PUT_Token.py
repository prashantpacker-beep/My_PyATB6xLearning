import requests
import pytest
import allure

base_url = "https://restful-booker.herokuapp.com/"
headers = {"Content-Type": "application/json"}
def get_token():
    base_path = "/auth"
    full_url= base_url+base_path
    json_payload_auth= {
    "username" : "admin",
    "password" : "password123"
}
    response_data= requests.post(url=full_url, json=json_payload_auth, headers=headers)
    print(response_data)
    assert response_data.status_code == 200
    response_data_json= response_data.json()
    token= response_data_json["token"]
    print(token)
    assert type(token)==str
    assert len(token)>0
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url + base_path

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=full_url, headers=headers, json=payload)
    assert response.status_code == 200

    response_json = response.json()
    booking_id = response_json["bookingid"]

    assert booking_id > 0
    return booking_id


def test_put_():
    token = get_token()
    booking_id = get_booking_id()

    base_path = f"/booking/ {booking_id}"
    full_url_put = base_url + base_path

    cookie = "token=" + token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Prashant",
        "lastname": "Kavinkar",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=full_url_put,headers=headers,json=json_payload)
    print(response.text)
    assert response.status_code == 200


    assert response.json()["firstname"] == "Prashant"
    assert response.json()["lastname"] == "Kavinkar"

def test_delete_():
    base_url = "https://restful-booker.herokuapp.com"
    booking_id = get_booking_id()

    delete_url = f"{base_url}/booking/{booking_id}"

    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }

    response = requests.delete(url=delete_url, headers=headers)

    print(response.status_code)
    assert response.status_code == 201 or response.status_code == 204

