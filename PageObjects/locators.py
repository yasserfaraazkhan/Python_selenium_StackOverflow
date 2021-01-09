from selenium.webdriver.common.by import By

class HomePage():
    _search_box = {'by': By.NAME, 'value': 'q'}
    _votes_option = {'by': By.XPATH, 'value': '//*[@data-value="votes"]'}
    _questions_count = {'by': By.XPATH, 'value': "//*[@data-position]"}
    _questions_link = lambda index: {'by': By.XPATH, 'value': "//*[@data-position][%s]/descendant::a[contains(text(),'Q:')]" % str(index)}
    _questions_votes_count = lambda index: {'by': By.XPATH, 'value': "//*[@data-position][%s]/descendant::span[@class='vote-count-post ']" % str(index)}
    _questions_answers_count = lambda index: {'by': By.XPATH, 'value': "//*[@data-position][%s]/descendant::div[contains(@class, 'answered')]/strong" % str(index)}
    _questions_post_tags = lambda index: {'by': By.XPATH, 'value': "//*[@data-position][%s]/descendant::a[@class='post-tag']" % str(index)}
    _votes_by_accepted_answer = {'by': By.XPATH, 'value': "//*[@itemprop='acceptedAnswer']/descendant::div[@itemprop='upvoteCount']"}
    _more_button = {'by': By.CSS_SELECTOR, 'value': 'nav.ps-relative'}
