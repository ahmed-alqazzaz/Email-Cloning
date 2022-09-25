from checkers.facebook_checker import FacebookChecker
from checkers.yahoo_checker import YahooChecker
from checkers.hotmail_checker import HotmailChecker
from utils.helper import Helper

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from dotenv import load_dotenv
import os
from time import sleep



class Cloner(YahooChecker,HotmailChecker,FacebookChecker,Helper):
    def __init__(self):
        #set up chrome driver options 
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches",["enable-automation"])
        option.add_experimental_option("useAutomationExtension","False")
        option.add_argument('--disable-blink-features=AutomationControlled')
        
        #export environment variable
        load_dotenv()
        
        #instantiate chrome driver
        PATH = rf"{os.getenv('CHROMEDRIVER_PATH')}"
        self.driver = webdriver.Chrome(executable_path = PATH,options = option)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)

        #add a second tab
        sleep(1.5)
        self.driver.execute_script("window.open('');")
    
    
    #username_composer will return nested list of possible usernames
    @staticmethod
    def username_composer():
        #assign first name if it only contains English letters and less than 15 chars
        if not (first_name := str(input("\nFirst Name: ")).strip()).isalpha() or len(first_name) > 15 :
            raise Exception("First Name is invalid")
        #assign last name if it only contains English letters and less than 15 chars
        if not (last_name := str(input("Last Name: ")).strip()).isalpha() or len(last_name) > 15 :
            raise Exception("Last Name is invalid")
        
        # declare a list that will contain iterators of usernames
        USERNAMES = []
        
        #append iterator of names
        
        USERNAMES.append(map(lambda i: f"{first_name}{last_name}{i}",range(200)))
        #result like ['willsmith0','willsmith1','willsmith2',..]

        USERNAMES.append(map(lambda i: f"{first_name}{last_name}.{i}",range(200)))
        #result like ['willsmith.0','willsmith.1','willsmith.2',..]
        
        USERNAMES.append(map(lambda i: f"{first_name}.{last_name}{i}",range(200)))
        #result like ['will.smith0','will.smith1','will.smith2',..]

        USERNAMES.append(map(lambda i: f"{first_name}_{last_name}{i}",range(200)))
        #result like ['will_smith0','will_smith1','will_smith2',..]

        USERNAMES.append(map(lambda i: f"{first_name}{last_name}_{i}",range(200)))
        #result like ['willsmith_0','willsmith_1','willsmith_2',..]

        USERNAMES.append(map(lambda i: f"{first_name}{i}",range(200)))
        #result like ['will0','will1','will2',..]

        USERNAMES.append(map(lambda i: f"{first_name}.{i}",range(200)))
        #result like ['will.0','will.1','will.2',..]

        USERNAMES.append(map(lambda i: f"{first_name}_{i}",range(200)))
        #result like ['will_0','will_1','will_2',..]

        USERNAMES.append(map(lambda i: f"{last_name}{i}",range(200)))
        #result like ['smith0','smith1','smith2',..]

        USERNAMES.append(map(lambda i: f"{last_name}.{i}",range(200)))
        #result like ['smith.0','smith.1','smith.2',..]

        USERNAMES.append(map(lambda i: f"{last_name}_{i}",range(200)))
        #result like ['smith_0','smith_1','smith_2',..]

        return USERNAMES
    
    @staticmethod
    def Domain():
        #return the selected mode in case user input is valid 
        if (Domain := str(input("\nDomain(Yahoo/Hotmail): ")).lower().strip()) in ["yahoo","hotmail"]: return Domain
        
        #in case user input is not in the list
        raise Exception("Domain is not valid") 
   
    #check if the user wants to type username or compose username
    @staticmethod
    def mode():
        #return the selected mode in case user input is valid 
        if (mode := str(input("Mode(Compose Username/Type Username): ")).upper().strip()) in ["COMPOSE USERNAME","TYPE USERNAME"]: return mode
        
        #in case user input is not in the list
        raise Exception("Mode is not valid") 

    
    #return username if it is not too long
    @staticmethod
    def get_username():
        if (len(username := str(input("\nUsername: ").strip()))) < 35 : return username
        print("username must be less than 35 characters")
        raise Exception("Username is too long")   