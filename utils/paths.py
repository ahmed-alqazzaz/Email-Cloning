PATHS = {}

PATHS["body"] = '//body'

PATHS["yahoo"] = {
    "EmailPlaceholder" : '//*[@id="usernamereg-userId"]',
    "RegistrationError":'//*[@id="reg-error-userId"]',
    "FullName" : '//*[@id="usernamereg-fullname"]',
    "SuggestionsList" : '//*[@id="desktop-suggestion-list"]',
    "Password": '//*[@id="usernamereg-password"]',
    "BirthDay" : '//*[@id="usernamereg-birthYear"]'
}

PATHS["hotmail"] = {
    "CreateAccount" : 'Create free account',
    "Domain": '//*[@id="CredentialsInputPane"]/fieldset/div[1]/div[3]/div[2]/div/div',
    "DomainBoxList": '//*[@id="LiveDomainBoxList"]',
    "EmailPlaceholder": '//*[@id="MemberName"]',
    "NextButton": '//*[@id="iSignupAction"]',
    "RegistrationError": '//*[@id="MemberNameError"]',
    "CancelSignup": '//*[@id="iSignupBannerCancel"]'
}

PATHS["facebook"] = {
    "ForgotMyPassword" : 'Forgot password?',
    "EmailPlaceholder" : '//input[@placeholder="Email or mobile number"]',
    "SearchButton" : '//button[@name="did_submit"]',
    "NoResultsMessage": "//div[text()='No Search Results']",
    "ResetYourPassword": "//h2[text()='Reset your password']",
    "NotYou": 'Not you?'
}