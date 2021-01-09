from Manager.PageInstace import ClassInstance


class Test_Search_Stackoverflow(ClassInstance):

    def test_search_stackoverflow(self):
        self.get_home_page().open('http://stackoverflow.com/')
        self.get_home_page().search('selenium webdriver')
        self.get_home_page().assert_search_results(15)
        self.get_home_page().sort_by_votes()
        self.get_home_page().print_question_votes_answers()
