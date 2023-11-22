Feature: Search for CCA details 
    Scenario: Search for "Badminton"
        Given Chrome browser is Launched
        When Open NP Website
        Then Select Student Life Tab
        Then Select Clubs and Society
        Then Select Sports 
        Then Select Badminton
        Then Verify if selected Badminton
        And Close browser