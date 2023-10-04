import allure
from allure_commons.types import Severity
from selene.api import *


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Alexey')
@allure.feature('Allure')
@allure.story('Allure with decorator')
def test_issue_is_exists_with_decorators():
    open_main_page()
    find_repo('eroshenkoam/allure-example')
    open_link_repo('eroshenkoam/allure-example')
    open_tab_issue()
    check_issue_exists('issue_to_test_allure_report')


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Найти репозиторий "{repo}"')
def find_repo(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Перейти в репозиторий "{repo}" по ссылке')
def open_link_repo(repo):
    browser.all('.search-match').element_by(have.exact_text(repo)).click()


@allure.step('Открыть таб "Issues"')
def open_tab_issue():
    browser.element('#issues-tab').should(be.visible).click()


@allure.step('Проверить наличие текста "{issue_text}" в issue')
def check_issue_exists(issue_text):
    browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text(issue_text)).should(be.visible)
