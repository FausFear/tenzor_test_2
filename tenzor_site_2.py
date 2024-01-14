from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

class SbisWebsite:
    def __init__(self, url):
        self.url = url
        self.browser = Chrome()
        self.region_css = "span[class='sbis_ru-Region-Chooser__text sbis_ru-link']"
        self.contacts_button_css = "a[href='/contacts']"

    # Открываем сайт
    def open(self):
        self.browser.get(self.url)
        time.sleep(3)

    # Нажимаем на кнопку
    def click_button(self, selector):
        button = self.browser.find_element(By.CSS_SELECTOR, selector)
        button.click()
        time.sleep(2)

    # Получаем элемент
    def get_element_text(self, selector):
        element = self.browser.find_element(By.CSS_SELECTOR, selector)
        return element.text

    # Получаем элементы со страницы в списке
    def get_elements_text(self, selector):
        elements = self.browser.find_elements(By.CSS_SELECTOR, selector)
        return [element.text for element in elements]

    # Изменяем регион
    def change_region(self, new_region):
        region_text = self.browser.find_element(By.CSS_SELECTOR, self.region_css)
        region_text.click()
        time.sleep(2)
        new_region = self.browser.find_element(By.CSS_SELECTOR, f"span[title='{new_region}']")
        new_region.click()
        time.sleep(2)
        return self.get_element_text(self.region_css)

    # Получаем список парнёров
    def get_current_partners(self):
        partners = self.browser.find_elements(By.CLASS_NAME, "sbisru-Contacts-List__name")
        return [name.text for name in partners]

    def check_partner_changes(self, original_partners):
        current_partners = self.get_current_partners()
        return current_partners != original_partners

    # Получаем заглавие сайта
    def get_title(self):
        return self.browser.title

    # Получаем текущий url
    def get_current_url(self):
        return self.browser.current_url

    # Закрываем браузер
    def close_browser(self):
        self.browser.quit()


def main():
    sbis = SbisWebsite("https://sbis.ru/")
    sbis.open()

    # Нажимаем на кнопку контакты и выводим текущий регион
    sbis.click_button(sbis.contacts_button_css)
    region = sbis.get_element_text(sbis.region_css)
    print("Текущий регион:", region)

#     Получаем и выводим список партнёров
    original_partners = sbis.get_current_partners()
    print("Список партнёров:", original_partners)

    # Меняем регион
    sbis.change_region("Камчатский край")

    # Выводим список партнёров в изменённом регионе
    changed_partners = sbis.get_current_partners()
    print("Изменённый список партнёров:", changed_partners)

    # Проверяем изменился ли список партнёров
    if sbis.check_partner_changes(original_partners):
        print("Список партнёров изменился")
    else:
        print("Список партнёров не изменился")

    # Проверяем title и url
    print("Заглавие:", sbis.get_title())
    print("URL:", sbis.get_current_url())

    sbis.close_browser()


if __name__ == "__main__":
    main()
