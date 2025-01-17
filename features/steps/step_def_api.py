import ast
import json
import os
import requests

from behave import given, when, then
from jsonschema import validate, ValidationError
from dotenv import load_dotenv
from config.endpoints import API_ENDPOINTS

load_dotenv()



def load_json_schema(file_path):
    """Loads a JSON schema from a given file path."""
    schema_path = os.path.join(os.path.dirname(__file__), '../../schemas', file_path)
    with open(schema_path, 'r') as file:
        return json.load(file)

def get_nested_value(data, keys):
    """Recursively fetches the value from a nested dictionary/list based on a list of keys."""
    for key in keys:
        # Handle array indices if present
        if key.isdigit():
            data = data[int(key)]
        else:
            data = data[key]
    return data

# @given('I have the API endpoint "{endpoint_key}" with param {params}')
# def define_api_endpoint(context, endpoint_key, params):
#     appid = os.getenv("OPENWEATHER_API_KEY")
#
#     if not appid:
#         raise ValueError("API key not found. Make sure it's set in the .env file.")
#
#     # Fetch the endpoint from the configuration using the key
#     endpoint = API_ENDPOINTS.get(endpoint_key)
#     if not endpoint:
#         raise ValueError(f"Endpoint key '{endpoint_key}' not found in configuration.")
#
#     # Convert params string to dictionary
#     params_dict = ast.literal_eval(params)
#
#     # Add the appid to the params dictionary
#     params_dict['appid'] = appid
#
#     # Print the endpoint and params for debugging
#     print(f"Endpoint: {endpoint}")
#     print(f"Params: {params_dict}")
#
#     context.base_url = endpoint
#     context.params = params_dict

@when('I send a GET request')
def send_get_request(context):
    context.response = requests.get(context.base_url, params=context.params)
    print(f"{context.response}")

@then('the response status code should be {expected_code:d}')
def check_status_code(context, expected_code):
    actual_code = context.response.status_code
    print(f"ini adalah code: {actual_code}")
    assert actual_code == expected_code, f"Expected status code {expected_code}, but got {actual_code}"



@given('I have the API endpoint "{endpoint_key}" with param {params}')
def define_api_endpoint(context, endpoint_key, params):
    """ Define API endpoint and parameters dynamically. """

    # Convert params from string to dictionary
    params_dict = ast.literal_eval(params)

    # Get the endpoint from API_ENDPOINTS
    endpoint = API_ENDPOINTS.get(endpoint_key)
    if not endpoint:
        raise ValueError(f"Endpoint key '{endpoint_key}' not found in configuration.")

    # Store endpoint and params in context for later use
    context.base_url = endpoint
    context.params = params_dict

    # Add headers (matching the cURL request)
    context.headers = {
        "accept": "application/json"
    }

    print(f"Base URL: {context.base_url}")
    print(f"Params: {context.params}")
    print(f"Headers: {context.headers}")

# @when('I send a GET request')
# def send_get_request(context):
#     """ Send a GET request using stored base URL and parameters. """
#     response = requests.get(context.base_url, params=context.params)
#     context.response = response  # Store response in context
#     print(f"Response: {response.status_code}")


# @then('the response status code should be {status_code:d}')
# def check_response_status_code(context, status_code):
#     """ Validate the response status code. """
#     assert context.response.status_code == status_code, \
#         f"Expected {status_code}, but got {context.response.status_code}"
#     print(json.dumps(status_code, indent=4))

@then('the response should contain the key "{key_path}" with value containing "{substring}"')
def check_dynamic_nested_response_contains(context, key_path, substring):
    json_data = context.response.json()
    keys = key_path.split('.')
    # print(json.dumps(json_data, indent=4)) for debugging

    # Get the value from the nested structure
    actual_value = get_nested_value(json_data, keys)

    # Validate that the actual value contains the substring
    assert substring in str(
        actual_value), f"Expected '{key_path}' value to contain '{substring}', but got '{actual_value}'"

@then('the response should have the key "{key_path}" with value {type} "{expected_value}"')
def check_dynamic_nested_response_contains(context, type, key_path, expected_value):
    """
    This step will check if the key_path in the response contains or does not contain the expected value.
    The 'type' can be 'contain' or 'not contain'.
    """
    json_data = context.response.json()
    keys = key_path.split('.')

    # Get the value from the nested structure
    actual_value = get_nested_value(json_data, keys)

    # Check if the type is to contain or not contain the value
    if type == "contain":
        assert expected_value in str(actual_value), \
            f"Expected '{key_path}' value to contain '{expected_value}', but got '{actual_value}'"
    elif type == "not contain":
        assert expected_value not in str(actual_value), \
            f"Expected '{key_path}' value to NOT contain '{expected_value}', but got '{actual_value}'"
    else:
        raise ValueError(f"Invalid type: {type}. Use 'contain' or 'not contain'.")

@then('the response should match the expected JSON schema from "{schema_source}"')
def validate_json_schema(context, schema_source):
    if schema_source.endswith('.json'):
        # If the schema source is a file path, load the schema from the file
        json_schema = load_json_schema(schema_source)
    else:
        # Otherwise, assume the schema source is a direct JSON string
        json_schema = json.loads(schema_source)

    json_data = context.response.json()

    try:
        validate(instance=json_data, schema=json_schema)
    except ValidationError as e:
        raise AssertionError(f"JSON schema validation error: {e.message}")


@when('User save response {path} as {var_name}')
def save_response_as(context, path, var_name):
    # Parse the response body using jsonpath_ng
    jsonpath_expr = ast.parse(path)
    result = [match.value for match in jsonpath_expr.find(context.response_body)]

    # Assuming you are using context to store the variable in the session
    context.vars[var_name] = result

    # only use print for development, comment again before commit
    # print(f"save response {var_name}: {result}")
