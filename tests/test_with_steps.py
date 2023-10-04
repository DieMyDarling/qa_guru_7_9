import allure
from allure_commons.types import Severity
from selene.api import *


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'Alexey')
@allure.feature('Allure')
@allure.story('Allure with decorator')
def test_issue_is_exists_with_steps():
    open_main_page()
    find_repo('eroshenkoam/allure-example')
    open_link_repo('eroshenkoam/allure-example')
    open_tab_issues()
    check_issue_exists('issue_to_test_allure_report')


def open_main_page():
    with allure.step('Открыть главную страницу'):
        browser.open('/')


def find_repo(repo):
    with allure.step('Найти репозиторий "{repo}"'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys(repo).press_enter()


def open_link_repo(repo):
    with allure.step('Перейти в репозиторий "{repo}" по ссылке'):
        browser.all('.search-match').element_by(have.exact_text(repo)).click()


def open_tab_issues():
    with allure.step('Открыть таб "Issues"'):
        browser.element('#issues-tab').should(be.visible).click()


def check_issue_exists(issue_text):
    with allure.step('Проверить наличие текста "{issue_text}" в issue'):
        browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text(issue_text)).should(be.visible)
