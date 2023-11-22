Feature: Search for Course Fees
    Scenario: Search for "fees"
        Given Chrome browser is Launched
        When Open NP Website
        Then Select navigation bar search button
        Then Input search query "fees"
        Then Select form search button
        Then Select course fees search result
        And Close browser

    