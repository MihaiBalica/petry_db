import requests
from typing import Any, Dict, Optional


def get_request(url: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
    """
    Makes a GET request to the specified URL with optional query parameters.

    :param url: The URL to send the GET request to.
    :param params: Optional query parameters to include in the GET request.
    :return: The response from the GET request.
    """
    return requests.get(url, params=params)


def post_request(url: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
    """
    Makes a POST request to the specified URL with an optional JSON payload.

    :param url: The URL to send the POST request to.
    :param json: Optional JSON payload to include in the POST request.
    :return: The response from the POST request.
    """
    return requests.post(url, json=json)


def put_request(url: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
    """
    Makes a PUT request to the specified URL with an optional JSON payload.

    :param url: The URL to send the PUT request to.
    :param json: Optional JSON payload to include in the PUT request.
    :return: The response from the PUT request.
    """
    return requests.put(url, json=json)


def delete_request(url: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
    """
    Makes a DELETE request to the specified URL with an optional JSON payload.

    :param url: The URL to send the DELETE request to.
    :param json: Optional JSON payload to include in the DELETE request.
    :return: The response from the DELETE request.
    """
    return requests.delete(url, json=json)


def validate_status_code(response: requests.Response, expected_code: int) -> None:
    """
    Validates that the response status code matches the expected status code.

    :param response: The response object from the request.
    :param expected_code: The expected HTTP status code.
    :raise AssertionError: If the response status code does not match the expected code.
    """
    assert response.status_code == expected_code, f"Expected status code {expected_code}, got {response.status_code}"


def validate_json_key_value_in_json_array(response: requests.Response, key: str, expected_value: Any) -> None:
    """
    Validates that the JSON response contains the specified key with the expected value.

    :param response: The response object from the request.
    :param key: The key to look for in the JSON response.
    :param expected_value: The expected value of the key.
    :raise AssertionError: If the key is not found or the value does not match the expected value.
    """
    json_data = response.json()[0]
    assert key in json_data, f"Key '{key}' not found in response"
    assert json_data[key] == expected_value, f"Expected {key} to be {expected_value}, got {json_data[key]}"
