*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  newusereee  validpassword123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
     Input Credentials  ab  validpassword123
     Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  user!@#  validpassword123
    Output Should Contain  All the characters aren't alphabet letters (a-z)

Register With Valid Username And Too Short Password
    Input Credentials  validuser  short
    Output Should Contain  Password must be at least 8 characters long

 Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  validuser  onlyletters
    Output Should Contain  Password must contain at least one non-letter character

*** Keywords ***
Input New Command And Create User
    Input New Command 
    Create User  kalle  kalle12345

