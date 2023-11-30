Feature: Look For Library in NP HomePage

    Scenario: Got to the Library button in NP HomePage
        Given Chrome browser is launched
        When Open NP Website
        Then Click on Library
        Then Verify Library is accessed
        And Close browser