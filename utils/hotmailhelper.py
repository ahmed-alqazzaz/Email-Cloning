
from selenium.webdriver.common.by import By
from utils.paths import PATHS
import random
from selenium.webdriver.support.ui import Select
from time import sleep

class HotmailHelper:
    def _create_account(self):
        #scroll down the page
        self.driver.execute_script("window.scrollTo(0,100)")
        
        #in case none of "create free account" buttons is not present within 5 seconds raise exception
        #if at least one of them is present present, assign the create_account_button variable to fullname placeholder selenium object
        if(create_account_button := self.get_element(5,(By.LINK_TEXT,PATHS["hotmail"]["CreateAccount"]),"presence",2)) is None:
            raise Exception("Create Free Account Button is not present")

        
        #if there is two buttons, index one of them randomly.
        if isinstance(create_account_button, list):
            create_account_button = create_account_button[random.randint(0, len(create_account_button) - 1 )]
        
        #hover over the button for some time then click 
        self.actions.move_to_element(create_account_button).pause(random.uniform(0.5,1.2)).perform()
        create_account_button.click()
    
    #set domain box to @hotmail.com
    def _change_domain(self):
        if (selected_domain := self.get_element(5,(By.XPATH,PATHS["hotmail"]["Domain"]), "presence")) is None:
            raise Exception("Domain Box is not present")

        #in case the selected domain is already hotmail
        if selected_domain.text.split("\n")[0] == "@hotmail.com":
            return


        
        #check if the domain box list is present
        if (domain_lst := self.get_element(5,(By.XPATH,PATHS["hotmail"]["DomainBoxList"]),"presence")) is None:
            raise Exception("Domain Box List is not present")
        #select hotmal.com in the domain box
        domain_lst = Select(domain_lst)
        domain_lst.select_by_index(1)
    
    #find the next button and click it
    def _submit_username(self):
        if (nxt_btn := self.get_element(5,(By.XPATH,PATHS["hotmail"]["NextButton"]),"presence")) is None:
            raise Exception("Next Button is not present")

        self.actions.move_to_element(nxt_btn).pause(random.uniform(0.5,1.2)).perform()
        nxt_btn.click()
    
    #find the cancel signup button and click it
    def _cancel_signup(self):
        if (cancel_signup_btn := self.get_element(5,(By.XPATH,PATHS["hotmail"]["CancelSignup"]),"presence")) is None:
            raise Exception("cancel signup Button is not present")

        self.actions.move_to_element(cancel_signup_btn).pause(random.uniform(0.5,1.2)).perform()
        cancel_signup_btn.click()