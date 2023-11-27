Feature: SignUpFeature

    Scenario: Successful Email Subcription Sign up on NP website
        Given Chrome browser is launched
        When Open NP homepage
        Then Input Email "jeromew489@frandin.com"
        Then Verify Successful Subcription
        And Close browser