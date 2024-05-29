from utils.api_utils import get_request, validate_status_code
from utils.step_context import given, when, then, also


def test_404_not_found(base_url, config):
    """
    Test for 404 Not Found error.
    """
    with given("an endpoint that doesn't exist"):
        endpoint = f"{base_url}{config['endpoints']['non_existent']}"
        expected_status_code = 404
    with when("the api is queried on this unknown endpoint"):
        response = get_request(endpoint)
    with then(f"the response is {expected_status_code}"):
        validate_status_code(response, expected_status_code)
