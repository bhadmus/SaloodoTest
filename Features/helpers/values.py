"""
This contains all values and selector items used in the main script.
To enable easy reference, reference, addition, or modification.
"""

# URLs

new_url = "https://demo.saloodo.com/dashboard"
url = "https://demo.saloodo.com"

# Registration Details

company_name = "The Time Piece"
phone = "+2348034591992"
first_name = "Tester"
last_name = "Saloodo"
email = "tester.saloodo@yopmail.com"

# Login Details (email will be reused)

password = "Password12@"

# Profile Page Details
vatId = "GB08034591992"
strt = "Burberry"
strtNo = "1491"
strNoAd = "Off Montgomery"
postCode = "50667"
city = "Cologne"

# Selectors for Registration and Login

company_field = "input[name='name']"
field_fname = "input[name='firstName']"
field_lname = "input[name='lastName']"
email_field = "input[name='email']"
phone_field = "input[name='phoneNumber']"
pwd_field = "_password"
username = "_email"
newsletter = ".newsletter .filter-checkbox"
terms = ".terms .filter-checkbox"
crBtn = ".btn.btn--big.btn--blue.btn--full-width"
formChk = ".shipper-form"
lgBtn = "LOGIN"
stBtn = "[type='submit']" # This is reused
popUp = ".modal--close span"

# Profile  Page Modification Selectors
prOpt = ".user-menu__name"
prGnl = "General"
editBtn = "div:nth-of-type(2) > .content > .details > .editBtn"
vatFld = "vatId"
strtFld = "street"
strtNoFld = "streetNo"
strNoAdFld = "streetNoAddition"
postFld = "postalCode"
cityFld = "city"
drp_down = ".is-clearable"
cntent = '//*[@id="react-select-3--option-4"]'
updated = "div:nth-of-type(2) > .content"
regBtn = ".btn--light-grey.btn--dropdown-button"