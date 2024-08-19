Feature: Weather Forecast And Air Polution

  @e2e-api @all @api1
  Scenario: Verify Get 5 day weather forecast of Jakarta Selatan
    Given I have the API endpoint "ENDPOINT_FORECAST" with param {"lat": "-6.225772", "lon": "106.858182"}
    When I send a GET request to the forecast API
    Then the response status code should be 200
    And the response should contain the key "city.name" with value containing "Jakarta Special Capital Region"
    And the response should match the expected JSON schema from "weather_api_schema.json"

  @e2e-api @all @api2
  Scenario: Verify Get current air pollution of Jakarta Selatan
    Given I have the API endpoint "ENDPOINT_AIR_POLLUTION" with param {"lat": "-6.225772", "lon": "106.858182"}
    When I send a GET request to the forecast API
    Then the response status code should be 200
    And the response should contain the key "list.0.main.aqi" with value containing "5"
    And the response should contain the key "list.0" with value containing "components"
    And the response should match the expected JSON schema from "air_pollution_schema.json"

