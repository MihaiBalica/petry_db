from utils.api_utils import get_request, validate_status_code, validate_json_key_value_in_json_array
from utils.step_context import given, when, then, also


def test_get_titles(base_url, config):
    with given("a title in the list is 'Young Lambs'"):
        expected_title = "Young Lambs"
        expected_number_of_titles = 10

    with when("the API is queried for title"):
        endpoint = f"{base_url}{config['endpoints']['title']}"
        response = get_request(endpoint)

    with then("the response status code should be 200"):
        validate_status_code(response, 200)

    with also(f"the number of titles returned should be at least {expected_number_of_titles}"):
        titles = response.json()['titles']
        assert len(titles) >= expected_number_of_titles, (f"Expected at least {expected_number_of_titles} titles, "
                                                        f"but got {len(titles)}")

    with also(f"the title \"{expected_title}\" should be in the list of titles"):
        titles = response.json()['titles']
        assert expected_title in titles, f"Expected title \"{expected_title}\" to be in the list of titles"

def test_get_specific_titles(base_url, config):
    with given("a title in the list is 'Last Words on Greece'"):
        expected_title = "Last Words on Greece"
        expected_author = "George Gordon, Lord Byron"

    with when("the API is queried for title"):
        endpoint = f"{base_url}{config['endpoints']['title']}/{expected_title}"
        response = get_request(endpoint)

    with then("the response status code should be 200"):
        validate_status_code(response, 200)

    with also(f"the title \"{expected_title}\" should have as author {expected_author}"):
        validate_json_key_value_in_json_array(response,'author', expected_author)