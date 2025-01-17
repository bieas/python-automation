Feature: Orange

  @web1 @web @all
  Scenario: Ensure user can login and logout
    Given user directs to url page "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    When user wait 5 seconds
    And user click field_user
    And user fill in field_user with "Admin"
    And user fill in field_pass with "admin123"
    And user click login_button
    And user wait 5 seconds until "Dashboard" visible in dashboard_menu
    And user click profile_btn
    And user click logout_btn
    And user wait 5 seconds
    Then field_user should be displayed
    And field_pass should be displayed

  @web2 @web @all
  Scenario: Ensure user cannot login with invalid credentials
    Given user directs to url page "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    When user wait 5 seconds
    And user click field_user
    And user fill in field_user with "sd"
    And user fill in field_pass with "sas"
    And user click login_button
    Then alert should be displayed

  @web3 @web @all
  Scenario: Ensure user cannot login without fill the username and password
    Given user directs to url page "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    When user wait 5 seconds
    And user click login_button
    Then required_alert_user should be displayed
    And required_alert_pass should be displayed
