# PoetryDB API Tests

This repository contains test cases for the PoetryDB API using pytest. The tests are designed to be modular, scalable, and follow best practices, including the Given-When-Then-And format for clear test steps.

## Project Structure

poetry_db/
├── README.md
├── tests/
│ ├── init.py
│ ├── test_author.py
│ ├── test_title.py
│ ├── test_errors.py
│ └── conftest.py
├── utils/
│ ├── init.py
│ ├── api_utils.py
│ └── step_context.py
├── config/
│ └── test_config.yaml
├── requirements.txt
├── pytest.ini
└── .env

- `tests/__init__.py`: Marks the `poetrydb_tests` directory as a Python package.
- `tests/test_author.py`: Contains test cases related to querying poems by author.
- `tests/test_title.py`: Contains test cases related to querying poems by title.
- `tests/test_errors.py`: Contains test cases for error handling.
- `tests/conftest.py`: Contains common fixtures and setup code for the tests.
- `utils/api_utils.py`: Contains utility functions for common API tasks.
- `utils/step_context.py`: Contains custom context managers for Given-When-Then-And steps.
- `config/test_config.yaml`: Configuration file for the tests. It is a plapcehoder in the current state
- `requirements.txt`: Lists the dependencies required to run the tests.
- `pytest.ini`: Configuration file for pytest.

## Test Cases

| Test Case Description                                  | Steps                                                                                                                      | Expected Result                                                                                                                                            |                                                                                    
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Verify that the API returns poems by a specific author | 1. Make a GET request to `/author/{author}`. <br> 2. Check the status code. <br> 3. Verify the number of poems.            | The API returns poems by the specified author. <br> Status code is 200. <br> The number of poems returned is greater than or equal to the expected number. |
| Verify that the API returns a specific poem by title   | 1. Make a GET request to `/title/{title}`. <br> 2. Check the status code. <br> 3. Verify the authors are the expected ones | The API returns the poem with the specified title. <br> Status code is 200. <br> The authors are in the response                                           |
| Verify that the API returns titles                     | 1. Make a GET request to `/title`. <br> 2. Check the status code. <br> 3. Verify the titles                                | The API returns many titles. <br> Status code is 200.                                                                                                      |

## Description

The purpose of the tests is to check:
- a happy path - which here is a valid GET request and a 200 return code and a JSON in the response with a specific format and content
  - two endpoints are tested for this case, the `/author` and `/title` 
- negative tests - which here is a GET request on an unknown endpoint, and we check that we receive a 404. 
  - In real life, for 40x tests there is also a response that has to be verified for specific keys and values

All the checks are being done with asserts, encapsulated in specific methods as many checks are going to be similar for all the endpoints.

### Validation

- **Status Code Validation**: Ensures that the request was successful and the API endpoint is functioning correctly.
- **Content Validation**: Checks the content of the response to ensure it matches the expected data (e.g., number of poems, author name). This ensures the API returns accurate and correct information.

## Running the Tests

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Run the tests:

```bash
pytest
```
or
```bash
pytest -v
```
or     
```bash
pytest -s -v
```