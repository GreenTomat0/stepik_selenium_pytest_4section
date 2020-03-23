import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="en", help="Choose language: ru or en")


@pytest.fixture(scope="function")
def language(request):
	user_language = request.config.getoption("language")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	return options

@pytest.fixture(scope="function")
def browser(language):
	print("\nstart browser for test..")
	browser = webdriver.Chrome(options=language)
	yield browser
	time.sleep(10)
	print("\nquit browser")
	browser.quit()