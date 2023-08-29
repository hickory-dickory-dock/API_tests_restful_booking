from assertpy import assert_that
import requests
import json
import endpoints
import config

import pdb

def test_create_booking():
    # Setup
    # No special setup needed for this test

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

    # Teardown
    # Undo what the test did, essentially delete the new entry
    booking_id = str(response["bookingid"])
    headers["Cookie"] = "token=" + config.get_token()
    teardown_response = requests.delete(url=endpoints.delete.replace("{id}", booking_id), headers=headers)
    assert_that(teardown_response.status_code).is_equal_to(requests.codes.created), "Error on delete, response code wasn't ok [200]: " + str(teardown_response.status_code)

def test_create_invalid_booking_dates_inverse():
    # Setup
    # No special setup needed for this test

    # Arrange
    headers = {"Content-Type": "application/json; charset=utf-8"}
    with open("Data/invalid_booking_dates_inverse.json", "r") as f:
        body = json.loads(f.read())

    # Act
    raw_response = requests.post(url=endpoints.booking, headers=headers, json=body)

    # Assert
    assert_that(raw_response.status_code).is_equal_to(requests.codes.bad_request), "Response code wasn't expected: " + str(raw_response.status_code)

    # Teardown
    # That should not have been saved, so technically no teardown

    