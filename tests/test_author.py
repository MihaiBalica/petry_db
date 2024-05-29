from utils.api_utils import get_request, validate_status_code, validate_json_key_value_in_json_array
from utils.step_context import given, when, then, also


def test_get_poems_by_author(base_url, config):
    with given("an author name is 'Jane Taylor'"):
        author = "Jane Taylor"
        expected_number_of_poems = 4
        expected_title = "The Holidays"

    with when("the API is queried for poems by the author"):
        endpoint = f"{base_url}{config['endpoints']['author']}{author}"
        print(endpoint)
        response = get_request(endpoint)

    with then("the response status code should be 200"):
        validate_status_code(response, 200)

    with also(f"the number of poems returned should be at least {expected_number_of_poems}"):
        poems = response.json()
        assert len(poems) >= expected_number_of_poems, (f"Expected at least {expected_number_of_poems} poems, "
                                                        f"but got {len(poems)}")

    with also(f"the title \"{expected_title}\" should be in the list of poems"):
        titles = [t['title'] for t in response.json()]
        assert expected_title in titles, f"Expected title \"{expected_title}\" to be in the list of poems"
