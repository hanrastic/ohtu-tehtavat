*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  joonaas
    Set Password  121212
    Set Password_confirmation  121212
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  j
    Set Password  121212
    Set Password_confirmation  121212
    Submit Credentials
    Register Should Fail With Message  Username is too short. Minimum lenght is 3


Register With Valid Username And Too Short Password
    Set Username  Jhones
    Set Password  12
    Set Password_confirmation  12
    Submit Credentials
    Register Should Fail With Message  Password is unvalid. Make sure password contains atleast 1 digit and is atleast 5 characters long.

Register With Nonmatching Password And Password Confirmation
    Set Username  Jeehaww
    Set Password  ok121212
    Set Password_confirmation  ok1212
    Submit Credentials
    Register Should Fail With Message  Passwords do not match together

Login After Successful Registration
    Set Username  joonaas
    Set Password  121212
    Set Password_confirmation  121212
    Submit Credentials
    Register Should Succeed
    Go To Ohtu Page
    Ohtu Page Should Be Open
    Move Back To Login
    Login Page Should Be Open
    Set Username  joonaas
    Set Password  121212
    Click Login
    Ohtu Page Should Be Open

Login After Failed Registration
    Set Username  jake
    Set Password  12
    Set Password_confirmation  12
    Submit Credentials
    Register Should Fail With Message  Password is unvalid. Make sure password contains atleast 1 digit and is atleast 5 characters long.
    Go To Login Page
    Set Username  jake
    Set Password  12
    Click Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Register

Move Back To Login
    Click Button  Logout

Click Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

#Test setup
Create User And Go To Register Page
    Create User  joonas  joonas280998
    Go To Register Page
    Register Page Should Be Open