Feature: Account creation

   Test checks if new user can create an account with valid email and password

   Scenario: New user can create account with minimal data provided
       Given User is on the "automationpractice.com" website
       When User click on the "Sign In" button
       And User provide valid email
       And User click on the "Create Account" button
       And User select "Mrs" radio button
       And User enter "John" as a first name
       And User enter "Doe" as a last name
       And User enter "testtesttest" as a password
       And User select "11-10-1990" as a date of birth
       And User select "820 Justin Wall Suite 993" as my address
       And User select city as my city
       And User select state
       And User enter postal code
       And User enter "12025550136" as phone number
       And User enter "14844731916" as mobile number
       And User enter address alias for future reference
       And User click on the "Register" button
       Then User account will be created

