from time import sleep
import random

from utils.paths import PATHS

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FacebookHelper:
    def _submit_email(self,EmailPlaceholder):
        #50% of the time submit the email form directly
        if random.randint(0,99) < 50:
            EmailPlaceholder.submit()
        
        #50% of the time click the search button to submit
        else:
            SearchButton = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located((By.XPATH,PATHS["facebook"]["SearchButton"]))
            )
            #if email SearchButton is not visible within 10 seconds raise exception
            #if it's visible,assign the SearchButton variable to SearchButton selenium object
            if (SearchButton := self.get_element(10,  (By.XPATH,PATHS['facebook']['SearchButton']),   "visibility")) is None:
                raise Exception("EmailPlaceholder is not visible")
            
            #hover over the element then click
            self.actions.move_to_element(SearchButton).pause(random.uniform(0.8,1.3)).perform()
            SearchButton.click()
    
    
    """" 
        check if the "no result" message is visible within 5 seconds
        if it's visibile returns True otherwise returns False
    """
    def _no_result_message(self):
        
        #if "no result" is not displayed
        if not self.get_element(5, (By.XPATH,PATHS["facebook"]["NoResultsMessage"]) ,"visibility"):
            return False
        # in case there is a message
        else:
            return True
    
    
    # return true if the reset your password form is displayed
    def _reset_password_from(self):
        
        #if "reset your password" form is not visible
        if not self.get_element(5, (By.XPATH,PATHS["facebook"]["ResetYourPassword"]) ,"visibility"):
            return False
        
        
        #if email NotYouButton is not visible within 10 seconds raise exception
        #if it's visible,assign the NotYouButton variable to NotYouButton selenium object
        sleep(random.uniform(0.5,1.5))
        if (NotYouButton := self.get_element(5  ,(By.LINK_TEXT,PATHS["facebook"]["NotYou"]), "visibility")) is None:
            raise Exception("'Not you' Button is not visible")
        
        
        #click "not you" button to return to the previus page
        self.actions.move_to_element(NotYouButton).pause(random.uniform(0.3,1.5)).perform()
        NotYouButton.click()
        
        #return true because the form was visible
        return True
        
        
