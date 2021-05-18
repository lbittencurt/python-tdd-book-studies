from selenium import webdriver
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
        self.fail('Finish the test.')


        # She is invited to insert a new task item immediately


        # She types "Buy peacock feathers" in a text box


        # When she hits enter, the page is updated and now the page list:
        # "1: Buy peacock feathers"


        # There is still a text box inviting you to add another item.
        # She inserts "Use peacoack feathers to make a fly".


        # The page updated again and now show two itens in the list


        # Edith asks herself if the website will remember her tasks list.
        # Then she realizes that website generated a unique URL for her


        # She access that URL and her task list still there.


        # Satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    