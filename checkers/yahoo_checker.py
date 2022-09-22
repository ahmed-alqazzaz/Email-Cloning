import random
from time import sleep

from selenium.webdriver.common.by import By

from utils.paths import PATHS
from utils.yahoohelper import YahooHelper

"""""
This class is intended to check if the yahoo email address is clonable
then check if it's linked with facebook account
"""""
class YahooChecker(YahooHelper):   
    """"
         this function will return True if the yahoo address is available
         and false if it is not
    """
    def __sign_up(self):
        
        self.driver.get("https://login.yahoo.com/account/create")
        #check if page is loaded
        #is_loaded is defined in utils\helper.py on line54
        if self.is_loaded() is False:
            raise Exception("Page is not loading")
        

    def check_username(self,username):
        # move to the first tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        #if not on sign up page go to sign up page
        if self.driver.current_url != "https://login.yahoo.com/account/create" :
            self.__sign_up()
        
        self.username = username
        
        #type the username in the username placeholder
        #_type_email is defined in utils\helper.py on line 60
        self._type_email(username,"yahoo")
        
        # wait and then click on the fullname placeholder so that "email is unavailable" message might show
        sleep(random.uniform(0.8,1.6))
        #fullname_click is defined in utils\yahoo_helper.py on line 10
        self.fullname_click()
       
        
        #occasionally and randomly click on the password or birthday placeholder
        if random.randint(0,100) < 20:
            sleep(random.uniform(0.7,1.3))
            #defined in utils\yahoo_helper.py on line 20
            self.bday_pwd_clicker()
        
        sleep(random.uniform(1.6,2.3))
        
        #get_one_of_elements is defined in helper.py on line 33
        #if any of registration error  message or suggestion list is visible return true 
        if (reg_error := self.get_one_of_elements(10,  (By.XPATH,PATHS["yahoo"]['RegistrationError']),   (By.XPATH,PATHS["yahoo"]["SuggestionsList"]))) is None:
            return True
        
        #if one of the email unavailable message or suggestion list is visible return false
        else:
            #in case the registration error is due to special characters
            if str(reg_error.get_attribute("data-error")) == "messages.SOME_SPECIAL_CHARACTERS_NOT_ALLOWED":
                print(reg_error.get_attribute("data-error"))
                raise Exception(f"{username} is invalid")
            
            return False

        

        

def main():
    YahooCheckers = YahooChecker()
    print(YahooCheckers.check_username("steve9"))
    sleep(random.randint(2,4))
    print(YahooCheckers.check_username("stevey34ghg"))
    
    
    sleep(30)
    YahooCheckers.driver.quit()

# if __name__ == "__main__":
#     main()




        

        
    


        