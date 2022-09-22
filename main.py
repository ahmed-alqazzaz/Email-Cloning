from cloner import Cloner

import colorama 

from time import sleep

def main():
    #assign global variable tmp to zero
    globals()["tmp"] = 0

    #in case the user opts to check possible usernames from first and last name
    if Cloner.mode() == "COMPOSE USERNAME":
        #loop through each list of usernames and map each element with ckeck function
        [list(map(check,usernames)) for usernames in Cloner.username_composer()]
        sleep(5)
        cloner.driver.quit()

    #in case the user opts to directly check if username is available
    else:
        username = Cloner.get_username()
        check(username)
        sleep(5)
        cloner.driver.quit()
        

def check(username):
    #initialize global variable
    global tmp;
    global cloner;
    
    #instantiate Cloner object if global cloner instance doesn't exist 
    if 'cloner' not in globals():
        cloner= Cloner()

    
    
    # if there is 5 consecutive available emails break the map iteration and move to other usernames list
    if tmp == 5:
        raise StopIteration
    
    #return the function and move to another username in the same list if email is not available
    if (yahoo_status := cloner.check_username(username)) is False:
        print(f"{colorama.Fore.MAGENTA}YAHOO   :",end="    ")
        print(f"{colorama.Fore.RED}{username}@yahoo.com")
        print(colorama.Style.RESET_ALL,end="")
        #set tmp to 0
        tmp = 0
    
    elif yahoo_status is True and (facebook_status := cloner.check_facebook(f"{username}@yahoo.com")) is False:
        print(f"\n{colorama.Fore.MAGENTA}YAHOO   :",end="    ")
        print(f"{colorama.Fore.GREEN}{username}@yahoo.com")
        print(f"{colorama.Fore.BLUE}FACEBOOK:",end="    ")
        print(f"{colorama.Fore.RED}{username}@yahoo.com",end="\n")
        print(colorama.Style.RESET_ALL)

        tmp += 1
    
    elif yahoo_status is True and facebook_status is True:
        print(f"\n{colorama.Fore.MAGENTA}YAHOO   :",end="    ")
        print(f"{colorama.Fore.GREEN}{username}@yahoo.com")
        print(f"{colorama.Fore.BLUE}FACEBOOK:",end="    ")
        print(f"{colorama.Fore.GREEN}{username}@yahoo.com",end="\n\n")
        print(colorama.Style.RESET_ALL)

        tmp += 1

    
if __name__ == "__main__":
    main()