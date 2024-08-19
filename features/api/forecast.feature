Feature: Weather Forecast And Air Polution

  @api @all
  Scenario: Verify Get 5 day weather forecast of Jakarta Selatan
    Given I have the API endpoint "ENDPOINT_FORECAST" with param {"lat": "-6.237232", "lon": "106.852936"}
    When I send a GET request to the forecast API
    Then the response status code should be 200
    And the response should contain the key "cod"
    And the response should match the expected JSON schema


