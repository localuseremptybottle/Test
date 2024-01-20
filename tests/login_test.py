from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import allure
import pytest
from pages.my_account_page import Myaccountpage
from random import randint
import names
from password_generator import PasswordGenerator


@pytest.mark.usefixtures("setup")

class TestLogin:
        #test do sprawdzania logowania
    @allure.step("Odpalenie testu logowania do konta")
    def test_LoginUserCorrect(self): #Bez opcji kasowania
        login ='wuj3khp@gmail.com'
        password = '13qeadzc'
        My_account_page = Myaccountpage(self.driver)
        My_account_page.open_page()
        My_account_page.switch_to_frame()
        assert My_account_page.is_logo_dsplayed()
        My_account_page.click_on_Signupbutton()
        assert My_account_page.is_Logintoyouraccount_displayed()
        My_account_page.log_in(login,password)
        assert My_account_page.is_loggedasis_displayed()

    def test_LoginUserinCorrect(self):  # Bez opcji kasowania
        login = 'wuj3khp@gmail.com'
        password = '13qeadzc3'
        My_account_page = Myaccountpage(self.driver)
        My_account_page.open_page()
        My_account_page.switch_to_frame()
        assert My_account_page.is_logo_dsplayed()
        My_account_page.click_on_Signupbutton()
        assert My_account_page.is_Logintoyouraccount_displayed()
        My_account_page.log_in(login, password)
        assert My_account_page.is_Loginisincorrect_displayed()



