Feature: User Information Page

  @uispec @uispec1 @all
  Scenario: verify layout component user information page
    Given user directs to user information page "https://flip-sample-form.onrender.com"
    Then field_title should be displayed
    And field_first_name should be displayed
    And field_middle_name should be displayed
    And field_first_name should be displayed
    And field_last_name should be displayed
    And field_email should be displayed
    And field_phone_number should be displayed
    And field_dob should be displayed
    And gender should be displayed
    And field_province should be displayed
    And field_city should be displayed
    And submit_button should be displayed

  @uispec @uispec2 @all
  Scenario: verify validation component in user information page
    Given user directs to user information page "https://flip-sample-form.onrender.com"
    When user click submit_button
    Then validation_first_name should be displayed
    And validation_middle_name should be displayed
    And validation_last_name should be displayed
    And validation_email should be displayed
    And validation_phone_number should be displayed
    And validation_dob should be displayed
    And validation_province should be displayed
    And validation_city should be displayed

  @e2e-web @all
  Scenario Outline: ensure user can submit user information
    Given user directs to user information page "https://flip-sample-form.onrender.com"
    When user click field_title
    And user click title_option_mr
    And user fill in field_first_name with "<first>"
    And user fill in field_middle_name with "<middle>"
    And user fill in field_last_name with "<last>"
    And user fill in field_email with "<email>"
    And user fill in field_phone_number with "<phone>"
    And user fill in field_dob with "<dob>"
    And user click field_province
    And user click <option_province>
    And user wait 5 seconds until "Select a city" visible in field_city
    And user click field_city
    And user click <option_city>
    And user click submit_button
    Then verify should be contain "<first>"
    And verify should be contain "<middle>"
    And verify should be contain "<last>"
    And verify should be contain "<email>"
    And verify should be contain "<phone>"
    And verify should be contain "<verify_dob>"
    And verify should be contain "<verify_province>"
    And verify should be contain "<verify_city>"
    And close_button should be displayed
    Examples:
      | first | middle | last   | email             | phone      | dob        | option_province        | option_city   | verify_dob      | verify_province | verify_city   |
      | bieas | kultur | sadewo | bieas@mail.com    | 1231231231 | 11/05/1994 | dki_province_option    | city_option_1 | 11 Mei 1994     | DKI Jakarta     | Jakarta Barat |
      | test  | flip   | bisa   | bisadong@mail.com | 0892737127 | 17/08/1994 | jateng_province_option | city_option_1 | 17 Agustus 1994 | Jawa Tengah     | Semarang      |


