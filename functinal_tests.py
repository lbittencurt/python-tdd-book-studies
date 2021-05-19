from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTests(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about an interesting new online application for
        # to-do lists. She decides to check out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices that the page title and the header mention to-do lists (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to insert a new task item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" in a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page is updated and now the page list:
        # "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting you to add another item.
        # She inserts "Use peacoack feathers to make a fly".
        self.fail('Finish the test!')

        # The page updated again and now show two itens in the list


        # Edith asks herself if the website will remember her tasks list.
        # Then she realizes that website generated a unique URL for her


        # She access that URL and her task list still there.


        # Satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    