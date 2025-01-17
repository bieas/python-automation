from selenium.webdriver.common.by import By

user_information_title = (By.CSS_SELECTOR, ".text-2xl")
field_title = (By.ID, "title")
field_user = (By.XPATH, "//input[@name='username']")
field_pass = (By.XPATH, "//input[@name='password']")
login_button = (By.CSS_SELECTOR, ".oxd-button")
dashboard_menu = (By.XPATH, "//a[.='Dashboard']")
profile_btn = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
logout_btn = (By.XPATH, "//a[.='Logout']")
alert = (By.CSS_SELECTOR, ".oxd-alert")
required_alert_user = (By.CSS_SELECTOR, ".oxd-form > div:nth-of-type(1) .oxd-text")
required_alert_pass = (By.CSS_SELECTOR, ".oxd-form > div:nth-of-type(2) .oxd-text")

