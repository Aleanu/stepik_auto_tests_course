def test_find_add_card_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        present_elem = True
    except:
        present_elem = False
    assert present_elem, "No add_card button on page"