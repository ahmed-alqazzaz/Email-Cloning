from time import sleep
import random


from utils.paths import PATHS
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Helper:
    #return Element selenium object if matches the state
    def get_element(self,time,location,state,num_of_elements = 1):
        #check of the state of the element is in the list
        if state  not in ["visibility","presence"]:
            raise Exception("Element State is not valid")
        
        #check if number of elements is less than 1
        if num_of_elements < 1:
            raise Exception("number of all elements must be 1 or higher")
        
        
        #in case the number of elements is 1 the criteria will apply for one element
        if num_of_elements == 1:
            criteria = f"EC.{state}_of_element_located(location)"
        #in case the number of elements is higher 1 the criteria will apply for all element
        else:
            criteria = f"EC.{state}_of_all_elements_located(location)"
       
       
        try:
            #wait until the element state matches the given critera
            #if it doesn't match within the time range "timeout" exception will be raised
            exec(f"""global Element; Element = WebDriverWait(self.driver,time).until(
                {criteria}
            )""")
            
        #if the exception is timeout then element state did not match
        except TimeoutException:
            return None
        # in case it matches return the element selenium object
        else:
            """
                in case Element variable is a selenium object return it
                in case the number of requested selenium objects is or equal higher than the length of the available elements return the whole list of selenium objects
                in case it's a list of objects and the number of requested objects is lower than the length of available elements return only the requested number of objects
            """
            return Element if not isinstance(Element,list) or num_of_elements >= len(Element) else Element[num_of_elements:]
    
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
        if not self.get_element(5,(By.XPATH,PATHS["body"]),"visibility"):
            return False
        return True
    
    #go to the email placeholder and type the email then return the placeholder object
    def _type_email(self,email,website):
        if website not in ["facebook","yahoo","hotmail"]:
            raise Exception("Invalid Website")
        
        #if email EmailPlaceholder is not visible within 10 seconds raise exception
        #if it's visible,assign the EmailPlaceholder variable to EmailPlaceholder selenium object
        if (EmailPlaceholder := self.get_element(10,  (By.XPATH,PATHS[website]['EmailPlaceholder']),   "visibility")) is None:
            raise Exception("EmailPlaceholder is not visible")
        
        #hover over the placeholder for some time then type the email 
        self.actions.move_to_element(EmailPlaceholder).pause(random.uniform(0.5,1.8)).perform()
        EmailPlaceholder.clear()
        sleep(random.uniform(0.7,1.4))
        EmailPlaceholder.send_keys(email)
        sleep(random.uniform(0.5,1.1))
        return EmailPlaceholder