from selenium import webdriver

browser = webdriver.Chrome(
	executable_path=r'/Users/johan/Dev-courses/Django-course/platzigram/functional_test/chromedriver'
)
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title


browser.close()
