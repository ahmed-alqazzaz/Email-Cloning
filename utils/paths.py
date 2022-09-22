PATHS = {}


PATHS["yahoo"] = {
    "EmailPlaceholder" : '//*[@id="usernamereg-userId"]',
    "body" : '//body',
    "RegistrationError":'//*[@id="reg-error-userId"]',
    "FullName" : '//*[@id="usernamereg-fullname"]',
    "SuggestionsList" : '//*[@id="desktop-suggestion-list"]',
    "Password": '//*[@id="usernamereg-password"]',
    "BirthDay" : '//*[@id="usernamereg-birthYear"]'
}
PATHS["facebook"] = {
    "body" : '//body',
    "ForgotMyPassword" : 'Forgot password?',
    "EmailPlaceholder" : '//input[@placeholder="Email or mobile number"]',
    "SearchButton" : '//button[@name="did_submit"]',
    "NoResultsMessage": "//div[text()='No Search Results']",
    "ResetYourPassword": "//h2[text()='Reset your password']",
    "NotYou": 'Not you?'
}