from selene import browser, be, have

def test_search_google_positive(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_ggogle_search_without_result_with_message(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('jkghjkty546ghbfgmfhy54hjg').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу jkghjkty546ghbfgmfhy54hjg ничего не найдено.'))
