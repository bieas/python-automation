import os

import requests
from dotenv import load_dotenv
from behave import given, when, then

# Load environment variables from the .env file
load_dotenv()

@given('the API endpoint is "{base_url}"')
def define_api_endpoint(context,base_url):
    context.url = os.getenv(base_url)
    print("base ini" + base_url)


@when(r'I send a GET request (with|without) the query parameters')
def send_get_request(context, type):
    query_params = {}

    if type == "with":
        for row in context.table:
            query_params[row['key']] = row['value']

    context.response = requests.get(context.url, params=query_params if query_params else None)

@then('the response status code should be {status_code:d}')
def step_then_check_status_code(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain a list of posts')
def step_then_check_response_content(context):
    json_response = context.response.json()
    assert isinstance(json_response, list)
    assert len(json_response) > 0

