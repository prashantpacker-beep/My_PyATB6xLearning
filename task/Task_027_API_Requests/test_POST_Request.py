import pytest
import allure
import requests



@allure.title("TC#01 Create Booking CRUD Positive")
@allure.description("Verify the Create Booking")
#@pytest.mark.crud
def test_create_booking_tc1():
    base_url= "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    headers = {
        "Content-Type": "application/json"
    }
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response_data= requests.post(url=full_url, headers=headers, json=payload)
    assert response_data.status_code == 200
    response_data_json = response_data.json()
    print(response_data)


# Booking ID > 0 AND firstname ="Jim"

    bookingID = response_data_json["bookingid"]
    firstname = response_data_json["booking"]["firstname"]
    print(bookingID)
    print(firstname)

    assert bookingID is not None
    assert bookingID > 0
    assert type(bookingID) == int

    assert type(firstname) == str
    assert firstname == "Jim"

    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

# https:// jsonpathfinder.com
    #x.booking.bookingdates.checkin



    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time = response_data.elapsed.total_seconds()
    assert time < 3




@allure.title("TC#02 Create Booking CRUD Negative")
@allure.description("Verify that the invalid payload booking is not created")
#@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url= "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    headers = {
        "Content-Type": "application/json"
    }
    payload = {}
    response= requests.post(url=full_url, headers=headers, json=payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"