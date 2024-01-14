import pytest
from tenzor_site_2 import SbisWebsite


@pytest.fixture
def sbis_instance():
    sbis = SbisWebsite("https://sbis.ru/")
    sbis.open()
    yield sbis
    sbis.close_browser()

# Тест на корректность региона
def test_region(sbis_instance):
    sbis_instance.click_button(sbis_instance.contacts_button_css)
    region = sbis_instance.get_element_text(sbis_instance.region_css)
    assert "Республика Башкортостан" in region

# Тест на смену региона
def test_change_region(sbis_instance):
    sbis_instance.click_button(sbis_instance.contacts_button_css)
    original_region = sbis_instance.get_element_text(sbis_instance.region_css)
    new_region = sbis_instance.change_region("Камчатский край")
    assert original_region != new_region

# Тест смена парнёров
def test_check_partner_changes(sbis_instance):
    sbis_instance.click_button(sbis_instance.contacts_button_css)
    original_partners = sbis_instance.get_current_partners()
    sbis_instance.change_region("Камчатский край")
    changed_partners = sbis_instance.get_current_partners()
    assert original_partners != changed_partners

# Тест смена url региона
def test_get_current_url(sbis_instance):
    sbis_instance.click_button(sbis_instance.contacts_button_css)
    sbis_instance.change_region("Камчатский край")
    current_url = sbis_instance.get_current_url()
    assert "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients" in current_url

