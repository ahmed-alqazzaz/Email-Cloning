from time import sleep
import random

from utils.paths import PATHS
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Helper:
    def get_element(self,time,location,state):
        #check of the state of the element is in the list
        if state  not in ["visibility","presence"]:
            raise Exception("Element State is not valid")
       
        try:
            #  wait until the element state matches
            # if it doesn't match within the time range "timeout" exception will be raised
            exec(f"""global Element; Element = WebDriverWait(self.driver,time).until(
                EC.{state}_of_element_located(location)
            )""")
            
        #if the exception is timeout then element state did not match
        except TimeoutException:
            return None
        # in case it matches return the element selenium object
        else:
            return Element
    
    #check if it least one of two elements is visible then return selenium object of the element
    def get_one_of_elements(self,time,location1,location2):
        try:
            # wait until the element state matches one of the two elements
            # if neither of them  match within the time range "timeout"exception will be raised
            Element = WebDriverWait(self.driver,time).until(
                lambda driver : EC.visibility_of_element_located(location1)(self.driver) or EC.visibility_of_element_located(location2)(self.driver)
            )

        #if the exception is timeout then this means that element state did not match
        except TimeoutException:
            return None
        # in case it matches return the element selenium object 
        else:
            return Element


    #check if page is loaded
    def is_loaded(self):
        if not self.get_element(5,(By.XPATH,PATHS["yahoo"]["body"]),"visibility"):
            return False
        return True
    
    #go to the email placeholder and type the email then return the placeholder object
    def _type_email(self,email,website):
        if website not in ["facebook","yahoo"]:
            raise Exception("Invalid Website")
        
        #if email EmailPlaceholder is not visible within 10 seconds raise exception
        #if it's visible,assign the EmailPlaceholder variable to EmailPlaceholder selenium object
        if (EmailPlaceholder := self.get_element(10,  (By.XPATH,PATHS[website]['EmailPlaceholder']),   "visibility")) is None:
            raise Exception("EmailPlaceholder is not visible")
        
        #hover over the placeholder for some time then type the email 
        self.actions.move_to_element(EmailPlaceholder).pause(random.uniform(0.5,1.8)).perform()
        EmailPlaceholder.clear()
        EmailPlaceholder.send_keys(email)
        sleep(random.uniform(0.5,1.8))
        return EmailPlaceholder

    
       




