#about np -->contact --> directions --> view virtual tour
#explore --> start here --> school of ict

Feature: Find School of ICT from Virtual Tour
    Scenario: Find ICT
        Given Chrome browser is Launched
        When Open NP Website
        Then Select About NP
        Then Select Directions
        Then Select View Virtual Tour
        Then Select Explore
        Then Select Start Here
        Then Select School of ICT
        And Close browser