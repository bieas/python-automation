Feature: Reqres In

    @e2e-api @all @api1
  Scenario: Verify Get user in reqres in
    Given I have the API endpoint "ENDPOINT_REQRES" with param {"page": 1, "per_page": 1}
    When I send a GET request
    Then the response status code should be 200
    And the response should contain the key "page" with value containing "1"
    And the response should contain the key "data.0.id" with value containing "1"
    And the response should match the expected JSON schema from "user.json"


