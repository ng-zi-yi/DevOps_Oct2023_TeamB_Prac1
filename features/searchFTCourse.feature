Feature: Search for Full Time Course
    Background: 
        Given Chrome browser is Launched
        When Open NP Website
        Then Navigate to Full-Time Courses
        Then Verify correct location and title

    Scenario Outline: Search for IT and IM
        Then Input "<course>"
        Then Select Search button
        Then Verify if able to Search parameter: "<courseName>","<nameElement>"
        And Close browser
    
    Examples:
        |course|courseName|nameElement|
        |Info|Information Technology (IT)|/html/body/main/section/div/div[3]/div/div/div/div/a/h3|
        |Immersive|Immersive Media (IM)|/html/body/main/section/div/div[3]/div/div/div/div/a/h3|

    Scenario: Filter by School
        Then Select School dropdown
        Then Click Dropdown List
        And Close browser
