from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	def should_be_login_url():
		return "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

	def should_be_login_form():
		LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
		return LOGIN_FORM

	def should_be_register_form():
		REGISTER_FORM = (By.CSS_SELECTOR, "#register_form_1")
		return REGISTER_FORM
