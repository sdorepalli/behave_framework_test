Feature: OrangeHRM Login 
    Scenario: Login to OrangeHRM with valid parameters
        Given I launch Chrome browser
        When I open orange HRM Homepage 
        And Enter Username "Admin" and password "admin123"
        And click on login button
        Then User must successfully login to the Dashboard page

     Scenario Outline: Login to OrangeHRM with multiple parameters
        Given I launch Chrome browser
        When I open orange HRM Homepage 
        And Enter Username "<username>" and password "<password>"
        And click on login button
        Then User must successfully login to the Dashboard page

        Examples:
            | username | password |
            | admin    | admin123 |
            | admin123 | admin    |
            | adminxyz | admin123 |
            | admin    | adminxyz |








