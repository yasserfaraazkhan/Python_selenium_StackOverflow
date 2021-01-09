from PageObjects.locators import HomePage
from SeleniumBase.WebActions import Selenium
from selenium.common.exceptions import *

class HomePageFunctions(Selenium):
    url =''

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.url = url
        self.get_url(url)

    def search(self, query):
        query = query.replace(' ', '+')
        self.get_url(self.url+'search?q=%s'% query)

    def print_votes_of_accepted_answer(self):
        try:
            print('Votes by accepted answer =>', self.get_text(HomePage._votes_by_accepted_answer))
        except NoSuchElementException:
            print("There is no accepted answer for this question")
            pass
        finally:
            self.driver.back()

    def assert_search_results(self, results_to_assert):
        results_count = len(self.find_elements(HomePage._questions_count))
        assert results_count == results_to_assert 

    def sort_by_votes(self):
        self.click_element(HomePage._more_button)
        self.click_element(HomePage._votes_option)

    def print_question_votes_answers(self):
        results = len(self.find_elements(HomePage._questions_count))
        for i in range(1, results):
            try:
                question_element = self.find_element(HomePage._questions_link(i))
                print(self.get_text(HomePage._questions_link(i)))
                print("Votes =>", self.get_text(HomePage._questions_votes_count(i)))
                print("Answers =>", self.get_text(HomePage._questions_answers_count(i)))
                post_tags = self.find_elements(HomePage._questions_post_tags(i))
                tags = []
                for tag in post_tags:
                    if tag.text!='selenium-webdriver': tags.append(tag.text)
                print("Tags => ", *tags, sep =',')
                question_element.click()
                self.print_votes_of_accepted_answer()
                print('\n')
            except NoSuchElementException:
                pass

