Feature: Search Bar Query
    Background:
        Given Chrome browser is Launched
        When Open NP Website
        Then Select navigation bar search button

    Scenario Outline: Sort search result by most recent
        Then Input search "<query>"
        Then Select form search button
        Then Select sort by most recent
        Then Select query search result
        And Close browser

    Examples:
    |query|
    |fees|
    |bursary|
    |plp minors|

    Scenario Outline: Filter search by selection
        Then Input search "<query>"
        Then Select form search button
        Then Filter "<filterSelection>"
        Then Select query search result
        And Close browser    

    Examples:
    |query|filterSelection|
    |plp minors|//*[@id="chkGeneral"]|
    |bursary|//*[@id="chkNews"]|
    |fees|//*[@id="chkCourses"]|





    