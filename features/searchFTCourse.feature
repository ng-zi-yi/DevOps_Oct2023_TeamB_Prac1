Feature: Search for Full Time Course
    Scenario: Search for "Information Techonology"
        Given Chrome browser is Launched
        When Open NP Website
        Then Navigate to Full-Time Courses
        Then Input Course Title
        Then Select Search button
        Then Verify if able to Search
        And Close browser

    # Scenario: 
    #     Given Chrome browser is Launched
    #     When Open NP Website
    #     Then 
    #     And Close browser