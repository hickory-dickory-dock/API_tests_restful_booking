from assertpy import assert_that
import requests
import json
import endpoints

import pdb

def test_create_booking():
    # Arrange
    headers = {"Content-Type": "application/json; charset=utf-8"}
    with open("Data/valid_booking.json", "r") as f:
        body = json.loads(f.read())

    # Act
    raw_response = requests.post(url=endpoints.booking, headers=headers, json=body)

    # Assert
    assert_that(raw_response.status_code).is_equal_to(requests.codes.ok), "Response code wasn't ok [200]: " + str(raw_response.status_code)
    response = raw_response.json()
    assert_that(response["bookingid"]).is_greater_than(0), "There's something wrong with the ID"
    assert_that(response["booking"]).is_equal_to(body), "There's something wrong with the response body"