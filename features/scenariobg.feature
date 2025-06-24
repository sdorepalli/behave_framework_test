Feature: OrangeHRM Login
    Background: common steps
        Given I launch browser 
        When I open Application
        And Enter valid username and password
        And click on login
    Scenario: Login to HRM Application 
        Then User must login to the Dashboard page

    Scenario: Search user
        When navigate to Search page
        Then Search page should display

    Scenario: Advanced Search user
        When navigate to Advanced Search page
        Then Advanced Search page should display

