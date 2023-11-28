Feature: Search for Full Time Course
    Background: 
        Given Chrome browser is Launched
        When Open NP Website
        Then Navigate to Full-Time Courses

    Scenario: Search for IT 
        Then Input "Info"
        Then Select Search button
        Then Verify if able to Search
        And Close browser

    Scenario Outline: Filter by School
        Then Select School dropdown
        Then Select "<School>"
        Then Select Search button
        Then Verify Filter "<schoolName>" same as "<schoolNamePath>"
        And Close browser

    Examples:
    |School|schoolNamePath|schoolName|
    |/html/body/main/section/div/div[2]/div[1]/div/div[2]/select/option[3]|/html/body/main/section/div/div[3]/div/div/div[1]/div/a/p|School of Design & Environment (DE)|
    |/html/body/main/section/div/div[2]/div[1]/div/div[2]/select/option[4]|/html/body/main/section/div/div[3]/div/div/div[1]/div/a/p|School of Engineering (SoE)|

