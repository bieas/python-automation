Feature: Weather Forecast And Air Polution

  @api
  Scenario: Verify Get 5 day weather forecast of Jakarta Selatan
    Given the API endpoint is "API_URL"
    When I send a GET request with the query parameters
      | key   | value                              |
      | "lat"   | "-6.237232"                        |
      | "lon"   | "106.852936"                       |
      | "appid" | "1b4d5bc620bcecf510bf796901d7e123" |
    Then the response status code should be 200