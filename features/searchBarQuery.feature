Feature: Search for "fees" first result
    Scenario: Search for "fees"
        Given Chrome browser is Launched
        When Open NP Website
        Then Select navigation bar search button
        Then Input search query "fees"
        Then Select form search button
        Then Select fees search result
        And Close browser

    Scenario: Search for "fees" using sort by most recent
        Given Chrome browser is Launched
        When Open NP Website
        Then Select navigation bar search button
        Then Input search query "fees"
        Then Select form search button
        Then Select sort by most recent
        Then Select fees search result
        And Close browser

    Scenario: Search for "fees" using filter courses
        Given Chrome browser is Launched
        When Open NP Website
        Then Select navigation bar search button
        Then Input search query "fees"
        Then Select form search button
        Then Filter courses
        Then Select fees search result
        And Close browser


    