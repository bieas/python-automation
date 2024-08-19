import ast
import json
import os

import requests
from behave import given, when, then
from jsonschema import validate, ValidationError
from dotenv import load_dotenv
from config.endpoints import API_ENDPOINTS

load_dotenv()


def load_json_schema(schema_file):
    schema_path = os.path.join(os.path.dirname(__file__), '../../schemas', schema_file)
    with open(schema_path, 'r') as file:
        return json.load(file)

@given('I have the API endpoint "{endpoint_key}" with param {params}')
def define_api_endpoint(context, endpoint_key, params):
    appid = os.getenv("OPENWEATHER_API_KEY")

    if not appid:
        raise ValueError("API key not found. Make sure it's set in the .env file.")

    # Fetch the endpoint from the configuration using the key
    endpoint = API_ENDPOINTS.get(endpoint_key)
    if not endpoint:
        raise ValueError(f"Endpoint key '{endpoint_key}' not found in configuration.")

    # Convert params string to dictionary
    params_dict = ast.literal_eval(params)

    # Add the appid to the params dictionary
    params_dict['appid'] = appid

    context.base_url = endpoint
    context.params = params_dict

@when('I send a GET request to the forecast API')
def send_get_request(context):
    context.response = requests.get(context.base_url, params=context.params)

@then('the response status code should be {expected_code:d}')
def check_status_code(context, expected_code):
    actual_code = context.response.status_code
    assert actual_code == expected_code, f"Expected status code {expected_code}, but got {actual_code}"

@then('the response should contain the key "cod"')
def check_response_contains(context):
    json_data = context.response.json()
    # print("Full JSON Response:", json.dumps(json_data, indent=2)) #for debug only
    assert "cod" in json_data, "Response does not contain 'cod' key"
    assert json_data["cod"] == "200", f"Expected 'cod' value 200, but got {json_data['cod']}"


@then('the response should match the expected JSON schema')
def validate_json_schema(context):
    # Load the schema from the file
    json_schema = load_json_schema('weather_api_schema.json')

    json_data = context.response.json()
    try:
        validate(instance=json_data, schema=json_schema)
    except ValidationError as e:
        raise AssertionError(f"JSON schema validation error: {e.message}")
