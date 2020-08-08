"""Functional test for the minimun viable app"""
# Utilities
import unittest
# selenium
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """ The New Visitor functional test. """

    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path=r'/Users/johan/Dev-courses/Django-course/platzigram/functional_test/chromedriver'
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # johan has hear about about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # he notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('finish the test!')
        # he is invited to enter a to-do item straight away
        # He types "Buy peacock features" into a text box
        # (johan's hooby is tying fly-fishing lures)
        # when he hits enter, the page updates and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        # There is still a text box inviting him to add another item.
        # He enters "Use peacock feathers to make a fly" (johan is very methodical)
        # The page updates again, and now shows both items on his list
        # Johan wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for his -- there is some
        # Explanatory text to that affect
        # He visits that URL - he to-do list os still there.
        # Satisfied, he goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
