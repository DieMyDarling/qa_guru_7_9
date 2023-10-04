import allure
from allure_commons.types import Severity
from selene.api import *


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'Alexey')
@allure.feature('Allure')
@allure.story('Selene only')
def test_issue_is_exists():
    browser.open('/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    browser.all('.search-match').element_by(have.exact_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').should(be.visible).click()
    (browser.all('[data-hovercard-type="issue"]').element_by(
        have.exact_text('issue_to_test_allure_report')).should(be.visible))
