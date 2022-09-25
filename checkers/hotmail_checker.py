from selenium.webdriver.common.by import By

from time import sleep
import random 

from utils.paths import PATHS
from utils.hotmailhelper import HotmailHelper



"""""
This class is intended to check if the hotmail address is clonable
then check if it's linked with facebook account
"""""
class HotmailChecker(HotmailHelper):
    def __sign_up(self):
        self.driver.get("https://outlook.live.com")
        #check if page is loaded
        #is_loaded is defined in utils\helper.py on line54
        if self.is_loaded() is False:
            raise Exception("Page is not loading")

        self._create_account()

    def check_hotmail(self,username):
        # move to the first tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        #in case not on signup page
        if "https://signup.live.com" not in self.driver.current_url:
            self.__sign_up()
        
        sleep(random.uniform(1.1,1.8))
        #change domain to @hotmail.com
        self._change_domain()
        
        #type and submit the email
        self._type_email(username,"hotmail")
        self._submit_username()
        
        sleep(random.uniform(0.93,1.35))
        #in case there is no registeration error
        if (reg_error := self.get_element(7,(By.XPATH,PATHS["hotmail"]["RegistrationError"]),"visibility")) is None:
            self._cancel_signup()
            return True
        
        else:
            #in case the registeraion error is happening due to invalid username
            if str(reg_error.text) == "Enter the email address in the format someone@example.com.":
                print("Special Characters are not allowed")
                raise Exception(f"{username} is Invalid")
            
            #in case the username is not available
            return False