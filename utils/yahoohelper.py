from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from utils.paths import PATHS
import random

class YahooHelper:
    def fullname_click(self):
        #in case fullname placeholder is not present within 5 seconds raise exception
        #if it's present,assign the fullname variable to fullname placeholder selenium object
        if(fullname := self.get_element(5,(By.XPATH,PATHS["yahoo"]["FullName"]),"presence")) is None:
            raise Exception("fullname placeholder is not present")

        #hover over the placeholder for some time then click 
        self.actions.move_to_element(fullname).pause(random.uniform(0.5,1.2)).perform()
        fullname.click()

    def bday_pwd_clicker(self):
        # randomly choose between birthday and password placeholder paths
        path = random.choice( [PATHS["yahoo"]["BirthDay"]  ,  PATHS["yahoo"]["Password"]] )
        
        if(bday_pwd := self.get_element(5,(By.XPATH,path),"presence")) is None:
            raise Exception("Birthday or Password placeholder is not present")

        #hover over the placeholder for some time then click 
        self.actions.move_to_element(bday_pwd).pause(random.uniform(0.5,1.8)).perform()
        
        try:
            bday_pwd.click()
        except ElementClickInterceptedException:
            print("Birthday or password placeholder is not clickable")      