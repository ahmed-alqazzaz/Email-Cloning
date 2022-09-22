from time import sleep
import random

from utils.paths import PATHS
from utils.facebookhelper import FacebookHelper

from selenium.webdriver.common.by import By



#this class is intended to check if there is a facebook account linked to the email 
class FacebookChecker(FacebookHelper):
    #direct the browser to "recover my facebook account" page
    def _recover_account(self):
        self.driver.get("https://facebook.com")
        #check if page is loaded
        if self.is_loaded() is False:
            raise Exception("Page is not loading")
        #if email ForgotMyPasswordButton is not visible within 10 seconds raise exception
        #if it's visible,assign the ForgotMyPasswordButton variable to ForgotMyPasswordButton selenium object
        if (ForgotMyPasswordButton := self.get_element(10,(By.LINK_TEXT,PATHS["facebook"]["ForgotMyPassword"]), "visibility")) is None:
            raise Exception("ForgotMyPasswordButton is not present")
        
        #hover on top of the element for about one second then click
        self.actions.move_to_element(ForgotMyPasswordButton).pause(random.uniform(0.3,1.5)).perform()
        ForgotMyPasswordButton.click()


    
    
    """"this function will return true if it is linked to fb account
    return false if it is not linked"""
    def check_facebook(self,email):
        # move to the second tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        try:
            #split out the unnecessary part of the url
            if self.driver.current_url.rsplit("/",1)[0] != "https://www.facebook.com/login/identify":
                #if the tab is not directed on the "recover your account" page execute the following
                self._recover_account()
        #in case the current url value is not splittable then attribute error will be raised
        except AttributeError:
            print("current page url is None") 
        
        
        #Type the email then submit the form
        #_type_email is defined in utils\helper.py on line 54
        EmailPlaceholder = self._type_email(email,"facebook")
        self._submit_email(EmailPlaceholder)
        
        sleep(random.uniform(0.4,1.1))
        #return true if both "no result" message was not  displayed and "reset your password" page is displayed
        return True if self._no_result_message() == False and self._reset_password_from() == True else False