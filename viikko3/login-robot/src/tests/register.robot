*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Kallee  123456789

Register With Already Taken Username And Valid Password
    Input Credentials  Joonas  12234243324
    Output Should Contain  User with username Joonas already exists

Register With Too Short Username And Valid Password
    Input Credentials  J  122344444
    Output Should Contain  Username is too short, minimum lenght is 3

Register With Valid Username And Too Short Password
    Input Credentials  Augusti  1234
    Output Should Contain  password is too short, minimum lenght is 8

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  Omaha  omahaomaha
    Output Should Contain  password has to contain atleast one digit

*** Keywords ***
Create User And Input New Command
    Create User  Joonas  1234567899
    Input New Command