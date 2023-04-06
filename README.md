# API_tests_restful_booking
API tests for the restful booking app (thanks to Mark Winteringham)

TC:
- Booking
     - Get booking IDs
        - All
        - Filter by name
        - Filter by checkin / checkout date
    - Get booking by ID
    - Create booking
    - Update booking
    - Partial update booking
    - Delete booking

How the tests were created

1. Take a look at what will be tested
2. Decide on what needs to be tested and how
3. Decide on a language, framework, libraries, etc
    - python due to simplicity
    - python with pytest, assertpy
    - requests for making API requests
4. 